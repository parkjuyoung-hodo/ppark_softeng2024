function doSomething() {
    let a = document.getElementById('inputA').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueC").innerHTML = Number(a) / Number(3.3);
}