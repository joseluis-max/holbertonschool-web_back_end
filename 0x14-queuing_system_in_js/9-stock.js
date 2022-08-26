import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

function getItemById(id) {
  return listProducts.filter(product => product.Id === id)[0];
}

const client = redis.createClient();

const clientGetAsync = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await clientGetAsync(itemId);
}

// express API
const express = require('express');

const app = express();

app.listen(1245);

const notFound = {"status":"Product not found"}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId)
  const stock = await getCurrentReservedStockById(itemId);
  const product = getItemById(itemId);

  if (product === null) {
    res.json(notFound);
  } else {
    product['currentQuantity'] = stock;
    res.json(product);
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  const stock = await getCurrentReservedStockById(itemId);
  const noStock = {
    "status": "Not enough stock available",
    "itemId": itemId
  }

  if (item === undefined) {
    res.json(notFound);
    return;
  }

  if (stock === null) {
    reserveStockById(itemId, item.initialAvailableQuantity - 1);
  } else {
    if (stock < 1) {
      res.json(noStock);
      return;
    }
    reserveStockById(itemId, stock - 1);
  }

  res.json({
    "status": "Reservation confirmed",
    "itemId": itemId
  });
});
