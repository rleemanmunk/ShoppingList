//Global Variables
var list = [];
var total = 0;

//Functions
function addToList(itemName, itemId, itemPrice) {
    var index = list.indexOf(itemId);
    if(index == -1) {
        $(".listItems").append("<li id='" + itemId + "'>" + itemName + "</li>");
        list.push(itemId);
        console.log(list);
        updateTotal(itemPrice, true);
    } else {
        $("li#" + itemId).remove(); 
        if (index > -1) {
            list.splice(index, 1);
        }
        updateTotal(itemPrice, false);
    }
}

function updateTotal(itemPrice, add) {
    if(add) {
        total = Number(total) + itemPrice;
    } else {
        total = Number(total) - itemPrice;
    }
    $("#total").empty();
    $("#total").append("$" + total);
}
