import createPushNotificationsJobs from "./8-job";
import { expect } from "chai";

const queue = require("kue").createQueue();

describe("is instance of array", () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it("with {} as argument", () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw("Jobs is not an array");
  });

  it("with Int 20 as argument", () => {
    expect(() => {
      createPushNotificationsJobs(20, queue);
    }).to.throw("Jobs is not an array");
  });

  it("with Bool true as argument", () => {
    expect(() => {
      createPushNotificationsJobs(true, queue);
    }).to.throw("Jobs is not an array");
  });

  it("with undefined as argument", () => {
    expect(() => {
      createPushNotificationsJobs(undefined, queue);
    }).to.throw("Jobs is not an array");
  });

  it("with null as argument", () => {
    expect(() => {
      createPushNotificationsJobs(null, queue);
    }).to.throw("Jobs is not an array");
  });
});

describe("expected", () => {
  it("with empty array [] as argument", () => {
    expect(createPushNotificationsJobs([], queue)).to.equal(undefined);
  });
});
