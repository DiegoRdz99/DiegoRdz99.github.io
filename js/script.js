var chds = { "C":0, "C♯":1,"D♭":1,"D":2,"D♯":3,"E♭":3, "E":4, "F":5,"F♯":6,"G♭":6, "G":7,"G♯":8,"A♭":8, "A":9,"A♯":10,"B♭":10, "B":11 }
var chds_sp = { 0:"C", 1:"C♯",2:"D",3:"D♯", 4:"E", 5:"F",6:"F♯", 7:"G",8:"G♯", 9:"A",10:"A♯", 11:"B" }
var chds_ft = { 0:"C",1:"D♭",2:"D",3:"E♭", 4:"E", 5:"F",6:"G♭", 7:"G",8:"A♭", 9:"A",10:"B♭", 11:"B" }
var btos = {"C♯":"D♭","D♯":"E♭","F♯":"G♭","G♯":"A♭","A♯":"B♭","D♭":"C♯","E♭":"D♯","G♭":"F♯","A♭":"G♯","B♭":"A♯"}

var output = document.getElementById("count")
var chords = document.getElementsByClassName("root")
var b_but = document.getElementById("b_but")
var capo_label = document.getElementById("tr-capo")
var qualities = document.getElementsByClassName("quality")
var diagrams = document.getElementsByClassName("fig")
var chord_names = document.getElementsByClassName("chord_name")
var trans = 0 // sets Transposition value to 0
var capo = false // sets transpose as standard (instead of capo)
var accidental = false // sets sharps as standard (instead of flats)
output.innerHTML = trans;
const base = []

function sign(a) {
    if (a<0) {
        return '-'+Math.abs(a).toString()
    }
    else if (a>0){
        return '+'+Math.abs(a).toString()
    }
    else {
        return "0"
    }
}

for (var i = 0; i < chords.length; i++) {
    base[i] = chords[i].innerHTML
}

mod = function (m, n) {
    return ((m % n) + n) % n;
};

function transpose() {
    for (var i = 0; i < chords.length; i++) {
        if (accidental) {
        chords[i].innerHTML = chds_ft[mod(chds[base[i]]+trans, 12)];
        chord_names[i].innerHTML = chds_ft[mod(chds[base[i]]+trans, 12)]+qualities[i].innerHTML;
    } else {
            chords[i].innerHTML = chds_sp[mod(chds[base[i]]+trans, 12)];
            chord_names[i].innerHTML = chds_sp[mod(chds[base[i]]+trans, 12)]+qualities[i].innerHTML;
        }
        diagrams[i].src = "../chords/"+chds_ft[mod(chds[base[i]]+trans, 12)].replace('♭','b')+qualities[i].innerHTML+".svg";
    }
    if (capo){output.innerHTML = -trans;}
    else {output.innerHTML = sign(trans);}
}

function tpup(){
    if (capo){trans = trans-1}
    else {trans = trans+1}
    transpose()
}

function tpdown(){
    if (capo){if (trans<0){trans = trans+1}}
    else {trans = trans-1}
    transpose()
}

function tr_capo(){
    if (trans<=0){
        capo = !capo
        if (capo) {
            capo_label.innerHTML = "Capo"
            output.innerHTML = -trans
        }
        else {
            capo_label.innerHTML = "Transpose"
            output.innerHTML = sign(trans)
        }
    }
}

function ft_sp(){
    accidental = !accidental
    if (accidental){
        b_but.classList = "b_true"
    }
    else {
        b_but.classList = "b_false"
    }
    for (var i = 0; i < chords.length; i++) {
        if (chords[i].innerHTML.length!=1){
        chords[i].innerHTML = btos[chords[i].innerHTML]
        chord_names[i].innerHTML = chords[i].innerHTML+qualities[i].innerHTML
        }
    }
}
