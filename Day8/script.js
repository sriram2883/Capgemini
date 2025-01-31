function update(obj){
    obj.name = "Jane";
}

var obj = new Object();
obj.name = "John";
obj.age = 30;
console.log("Before update: ", obj);
update(obj);
console.log("After update: ", obj);