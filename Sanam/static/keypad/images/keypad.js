function off(picname) {
    document.getElementById(picname).style.visibility = "hidden";
    document.getElementById(picname + "2").style.visibility = "visible";
}
function on(picn) {
    document.getElementById(picn).style.visibility = "visible";
    document.getElementById(picn + "2").style.visibility = "hidden";
}

function addText(btnId) {
    var txtLen = document.getElementById(targetTextId).value.length;
    var maxLen = document.getElementById(targetTextId).maxLength;


    if (txtLen >= maxLen) {
        tabNext();
    }
//                document.getElementById(targetTextId).value="123";
    var inputType = document.getElementById(targetTextId).getAttribute("type");
    if (inputType == "submit" || inputType == "button")
        return;
    var btnStr = document.getElementById(btnId).src;
    var num = btnStr.substr(btnStr.length - 9, 1);
    if (num == "1") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "1";
    } else if (num == "2") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "2";
    } else if (num == "3") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "3";
    } else if (num == "4") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "4";
    } else if (num == "5") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "5";
    } else if (num == "6") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "6";
    } else if (num == "7") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "7";
    } else if (num == "8") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "8";
    } else if (num == "9") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "9";
    } else if (num == "0") {
        document.getElementById(targetTextId).value = document.getElementById(targetTextId).value + "0";
    }
    var size = document.getElementById(targetTextId).maxLength;
    if (document.getElementById(targetTextId).value.length == size) {
        var tabI = document.getElementById(targetTextId).getAttribute('tabIndex');
        var elems = document.getElementsByTagName('input');
        for (var i = 0; i < elems.length; i++) {
            var ta = (elems[i].getAttribute('tabIndex'));
            if ((Number(tabI) + 1) == ta) {
                //                        alert(elems[i].id);
                targetTextId = elems[i].id;
                break;
            }
        }
    }
    document.getElementById(targetTextId).focus();
}

function deletText() {
    var inputType = document.getElementById(targetTextId).getAttribute("type");
    if (inputType == "submit" || inputType == "button")
        return;
    document.getElementById(targetTextId).value = document.getElementById(targetTextId).value.substr(0, document.getElementById(targetTextId).value.length - 1);
    document.getElementById(targetTextId).focus();
}

function tabNext() {
    var tabI = document.getElementById(targetTextId).getAttribute('tabIndex');
    var elems = document.getElementsByTagName('input');
    for (var i = 0; i < elems.length; i++) {
        var ta = (elems[i].getAttribute('tabIndex'));
        if ((Number(tabI) + 1) == ta) {
            //                        alert(elems[i].id);
            targetTextId = elems[i].id;
            break;
        }
    }
    document.getElementById(targetTextId).focus();
}

function tabLast() {
    var tabI = document.getElementById(targetTextId).getAttribute('tabIndex');
    var elems = document.getElementsByTagName('input');
    for (var i = 0; i < elems.length; i++) {
        var ta = (elems[i].getAttribute('tabIndex'));
        if ((Number(tabI) - 1) == ta) {
            //                        alert(elems[i].id);
            targetTextId = elems[i].id;
            break;
        }
    }
    document.getElementById(targetTextId).focus();
}

function setFocus() {
    document.getElementById(targetTextId).focus();
}


function setTargetFocus(val) {
    targetTextId = val;
}