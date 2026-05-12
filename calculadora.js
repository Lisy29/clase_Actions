const [a, b] = process.argv.slice(2).map(Number);
console.log(`Suma: ${a+b} | Resta: ${a-b} | Multiplicación: ${a*b} | División: ${b?a/b:"Error"}`);
