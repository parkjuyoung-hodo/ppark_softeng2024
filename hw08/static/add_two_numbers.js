function doSomething() {
    let a = document.getElementById('inputA').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueC").innerHTML = (Number(a) / 3.3).toFixed(2);
}