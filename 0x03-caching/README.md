# Caching

## General

**What a caching system is**
A CPU cache is a hardware cache used by the central processing unit (CPU) of a computer to reduce the average cost (time or energy) to access data from the main memory. A cache is a smaller, faster memory, located closer to a processor core, which stores copies of the data from frequently used main memory locations.
In computing, cache algorithms (also frequently called cache replacement algorithms or cache replacement policies) are optimizing instructions, or algorithms, that a computer program or a hardware-maintained structure can utilize in order to manage a cache of information stored on the computer.
**What FIFO means**
Using this algorithm the cache behaves in the same way as a FIFO queue. The cache evicts the blocks in the order they were added, without any regard to how often or how many times they were accessed before.
**What LIFO means**
Using this algorithm the cache behaves in the same way as a stack and opposite way as a FIFO queue. The cache evicts the block added most recently first without any regard to how often or how many times it was accessed before.
**What LRU means**
Discards the least recently used items first.
**What MRU means**
Discards the most recently used items first
**What LFU means**
Counts how often an item is needed. Those that are used least often are discarded first. This works very similar to LRU except that instead of storing the value of how recently a block was accessed, we store the value of how many times it was accessed.
**What the purpose of a caching system**
reduce the average cost (time or energy) to access data from the main memory.
**What limits a caching system have**

- Disadvantages of Cache Memory
  - [x] It is quite expensive.
  - [x] The storage capacity is limited.
