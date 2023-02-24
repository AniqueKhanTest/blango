class Greeter {
  constructor(name) {
    this.name = name;
  }
  getGreeting() {
    if (this.name === undefined) {
      return "Hello , no name";
    }
    return "Hello , " + this.name;
  }
  showGreeting(greetingMsg) {
    console.log(greetingMsg);
  }
  greet() {
    this.showGreeting(this.getGreeting());
  }
}
// const g = new Greeter();
// g.greet();

// Inheritance
class DelayedGreeter extends Greeter {
  delay = 2000;
  constructor(name, delay) {
    super(name);
    if (delay !== undefined) {
      this.delay = delay;
    }
  }
  greet() {
    setTimeout(() => {
      this.showGreeting(this.getGreeting());
    }, this.delay);
  }
}

const g = new DelayedGreeter("John");
g.greet();

const g2 = new DelayedGreeter("Jacob", 5000);
g2.greet();
