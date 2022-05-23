var chds = { "C":0, "C♯":1,"C♯":1,"D♭":1,"D":2,"D♯":3,"E♭":3, "E":4, "F":5,"F♯":6,"G♭":6, "G":7,"G♯":8,"A♭":8, "A":9,"A♯":10,"B♭":10, "B":11 }
var chds_sp2 = { 0:"C", 1:"C♯",2:"D",3:"D♯", 4:"E", 5:"F",6:"F♯", 7:"G",8:"G♯", 9:"A",10:"A♯", 11:"B" }
var chds_ft2 = { 0:"C",1:"D♭",2:"D",3:"E♭", 4:"E", 5:"F",6:"G♭", 7:"G",8:"A♭", 9:"A",10:"B♭", 11:"B" }
var chds_sp = { "C":0, "C♯":1,"D":2,"D♯":3, "E":4, "F":5,"F♯":6, "G":7,"G♯":8,"A":9,"A♯":10, "B":11 }
var chds_ft = { "C":0, "D♭":1,"D":2,"E♭":3, "E":4, "F":5,"G♭":6, "G":7,"A♭":8, "A":9,"B♭":10, "B":11 }
var btos = {"C♯":"D♭","D♯":"E♭","F♯":"G♭","G♯":"A♭","A♯":"B♭","D♭":"C♯","E♭":"D♯","G♭":"F♯","A♭":"G♯","B♭":"A♯"}

var output = document.getElementById("demo")
var chords = document.getElementsByClassName("root")
var qualities = document.getElementsByClassName("quality")
var diagrams = document.getElementsByClassName("fig")
var chord_names = document.getElementsByClassName("chord_name")
var toggle = document.getElementById('toggle')
var trans = 0
var capo = true
output.innerHTML = 0;
const base = []

for (var i = 0; i < chords.length; i++) {
    base[i] = chords[i].innerHTML
}

mod = function (m, n) {
    return ((m % n) + n) % n;
};

function transpose() {
    if (toggle.checked){
        for (var i = 0; i < chords.length; i++) {
            chords[i].innerHTML = chds_ft2[mod(chds_ft[base[i]]+trans, 12)];
            diagrams[i].src = "./.chords/"+chds_ft2[mod(chds_ft[base[i]]+trans, 12)].replace('♯','#').replace('♭','b')+qualities[i].innerHTML+".svg";
            chord_names[i].innerHTML = chds_ft2[mod(chds_ft[base[i]]+trans, 12)]+qualities[i].innerHTML;
            output.innerHTML = trans;
        }
    } else {
        for (var i = 0; i < chords.length; i++) {
            chords[i].innerHTML = chds_sp2[mod(chds_sp[base[i]]+trans, 12)];
            diagrams[i].src = "./.chords/"+chds_sp2[mod(chds_sp[base[i]]+trans, 12)].replace('♯','&').replace('♭','b')+qualities[i].innerHTML+".svg";
            chord_names[i].innerHTML = chds_sp2[mod(chds_sp[base[i]]+trans, 12)]+qualities[i].innerHTML;
            output.innerHTML = trans;
        }
    }
}

function tpup(){
    trans = trans+1
    transpose()
}

function tpdown(){
    trans = trans-1
    transpose()
}

function tr_capo(){
    capo = !capo
}

toggle.onclick = function() {
    for (var i = 0; i < chords.length; i++) {
        if (chords[i].innerHTML.length!=1){
        chords[i].innerHTML = btos[chords[i].innerHTML]
        chord_names[i].innerHTML = chords[i].innerHTML+qualities[i].innerHTML
        }
    }
    // transpose()
}