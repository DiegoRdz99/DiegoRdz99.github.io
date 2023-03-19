var chds = { "C": 0, "C♯": 1, "D♭": 1, "D": 2, "D♯": 3, "E♭": 3, "E": 4, "F": 5, "F♯": 6, "G♭": 6, "G": 7, "G♯": 8, "A♭": 8, "A": 9, "A♯": 10, "B♭": 10, "B": 11 };
var chds_sp = { 0: "C", 1: "C♯", 2: "D", 3: "D♯", 4: "E", 5: "F", 6: "F♯", 7: "G", 8: "G♯", 9: "A", 10: "A♯", 11: "B" };
var chds_ft = { 0: "C", 1: "D♭", 2: "D", 3: "E♭", 4: "E", 5: "F", 6: "G♭", 7: "G", 8: "A♭", 9: "A", 10: "B♭", 11: "B" };
var btos = { "C♯": "D♭", "D♯": "E♭", "F♯": "G♭", "G♯": "A♭", "A♯": "B♭", "D♭": "C♯", "E♭": "D♯", "G♭": "F♯", "A♭": "G♯", "B♭": "A♯" };
var output = document.getElementById("count");
var chords = document.getElementsByClassName("root");
var b_but = document.getElementById("b_but");
var dark_but = document.getElementById("dark-toggle");
var play_but = document.getElementById("play-but");
var capo_label = document.getElementById("tr-capo");
var qualities = document.getElementsByClassName("quality");
var diagrams = document.getElementsByClassName("fig");
var backsteps = (diagrams[0].src).split("chords")[0];
var chord_names = document.getElementsByClassName("chord_name");
var trans = 0; // sets Transposition value to 0
var capo = false; // sets transpose as standard (instead of capo)
var accidental = true; // sets sharps as standard (instead of flats)
var dark = false; // dark mode is set to false default;
var play = false; // autoscroll is set to false default;
output.innerHTML = trans;
const base = [];

var abcScore = document.getElementById('abc-score');
if (window.innerWidth < 500) {
    abcScore.innerHTML.replace('pagewidth 18cm','pagewidth 10cm');
    console.log('xd')
}


function sign(a) {
    if (a < 0) {
        return '-' + Math.abs(a).toString()
    }
    else if (a > 0) {
        return '+' + Math.abs(a).toString()
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
            chords[i].innerHTML = chds_ft[mod(chds[base[i]] + trans, 12)];
            chord_names[i].innerHTML = chds_ft[mod(chds[base[i]] + trans, 12)] + qualities[i].innerHTML;
        } else {
            chords[i].innerHTML = chds_sp[mod(chds[base[i]] + trans, 12)];
            chord_names[i].innerHTML = chds_sp[mod(chds[base[i]] + trans, 12)] + qualities[i].innerHTML;
        }
        diagrams[i].src = backsteps + "chords/" + chds_ft[mod(chds[base[i]] + trans, 12)].replace('♭', 'b') + qualities[i].innerHTML + ".svg";
    }
    if (capo) { output.innerHTML = -trans; }
    else { output.innerHTML = sign(trans); }
}

function tpup() {
    if (capo) { trans = trans - 1 }
    else { trans = trans + 1 }
    transpose()
}

function tpdown() {
    if (capo) { if (trans < 0) { trans = trans + 1 } }
    else { trans = trans - 1 }
    transpose()
}

function tr_capo() {
    if (trans <= 0) {
        capo = !capo
        if (capo) {
            capo_label.innerHTML = "Cp"
            output.innerHTML = -trans
        }
        else {
            capo_label.innerHTML = "Tp"
            output.innerHTML = sign(trans)
        }
    }
}

function ft_sp() {
    accidental = !accidental
    if (accidental) {
        b_but.innerHTML = '<span class="icon">&flat;</span>';
        // b_but.classList = "b_true";
    }
    else {
        // b_but.classList = "b_false"
        b_but.innerHTML = '<span class="icon">&sharp;</span>';
    }
    for (var i = 0; i < chords.length; i++) {
        if (chords[i].innerHTML.length != 1) {
            chords[i].innerHTML = btos[chords[i].innerHTML]
            chord_names[i].innerHTML = chords[i].innerHTML + qualities[i].innerHTML
        }
    }
}



function autoScroll() {
    window.scrollBy(0, 1);
}
let scroll = true;
function startInverval() {
    if (scroll) {
        play_but.innerHTML = '<span class="icon">&#x23f8;</span>'
        scrolldelay = setInterval(autoScroll, 100);
    }
    else {
        play_but.innerHTML = '<span class="icon">&#9654;</span>'
        clearInterval(scrolldelay);
    }
    scroll = !scroll;
}

function toggleDark() {
    if (dark) {
        dark_but.innerHTML = '<span class="icon">&#9788;</span>'
    }
    else {
        dark_but.innerHTML = '<span class="icon">&#9789;</span>'
    }
    dark = !dark;
    var element = document.body;
    element.classList.toggle("dark-mode");
    var tds = document.getElementsByClassName("lyricsline")
    for (let i = 0; i < tds.length; i++) {
        tds[i].classList.toggle("dark-mode");
    }
    var tds = document.getElementsByClassName("chord")
    for (let i = 0; i < tds.length; i++) {
        tds[i].classList.toggle("dark-chord");
    }
    var tds = document.getElementsByClassName("second_voice")
    for (let i = 0; i < tds.length; i++) {
        tds[i].classList.toggle("dark-2line");
    }
}