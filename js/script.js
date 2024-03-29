var chds = { "C": 0, "C♯": 1, "D♭": 1, "D": 2, "D♯": 3, "E♭": 3, "E": 4, "F": 5, "F♯": 6, "G♭": 6, "G": 7, "G♯": 8, "A♭": 8, "A": 9, "A♯": 10, "B♭": 10, "B": 11 };
var chds_sp = { 0: "C", 1: "C♯", 2: "D", 3: "D♯", 4: "E", 5: "F", 6: "F♯", 7: "G", 8: "G♯", 9: "A", 10: "A♯", 11: "B" };
var chds_ft = { 0: "C", 1: "D♭", 2: "D", 3: "E♭", 4: "E", 5: "F", 6: "G♭", 7: "G", 8: "A♭", 9: "A", 10: "B♭", 11: "B" };
var btos = { "C♯": "D♭", "D♯": "E♭", "F♯": "G♭", "G♯": "A♭", "A♯": "B♭", "D♭": "C♯", "E♭": "D♯", "G♭": "F♯", "A♭": "G♯", "B♭": "A♯" };
var output = document.getElementById("count");
var chords = document.getElementsByClassName("root");
var dark_but = document.getElementById("dark-toggle");
var play_but = document.getElementById("play-but");
var capo_label = document.getElementById("tr-capo");
var qualities = document.getElementsByClassName("quality");
var diagrams = document.getElementsByClassName("fig");
var backsteps = (diagrams[0].src).split("chords")[0];
var chord_names = document.getElementsByClassName("chord_name");
var bass_elements = document.getElementsByClassName("bass");
var song_key = (document.getElementById('song-key').innerHTML).replace("Clave: ", "");
var trans = 0; // sets Transposition value to 0
var capo = false; // sets transpose as standard (instead of capo)
var accidental = false; // sets sharps as standard (instead of flats)
var dark = false; // dark mode is set to false default;
// toggleDark();
var play = false; // autoscroll is set to false default;
output.innerHTML = trans;
const base = [];
const bass_notes = [];


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

/* Assign the base notes to the base Array */
for (var i = 0; i < chords.length; i++) {
    base[i] = chords[i].innerHTML
}

/* Assign the bass notes to the bass_notes array */
for (var i = 0; i < bass_elements.length; i++) {
    bass_notes[i] = bass_elements[i].innerHTML
}

mod = function (m, n) {
    return ((m % n) + n) % n;
};

function transpose() {
    /* Transpose chords */
    var output = document.getElementById("count");
    for (var i = 0; i < base.length; i++) {
        if (accidental) {
            chords[i].innerHTML = chds_ft[mod(chds[base[i]] + trans, 12)];
            chord_names[i].innerHTML = chds_ft[mod(chds[base[i]] + trans, 12)] + qualities[i].innerHTML;
        } else {
            chords[i].innerHTML = chds_sp[mod(chds[base[i]] + trans, 12)];
            chord_names[i].innerHTML = chds_sp[mod(chds[base[i]] + trans, 12)] + qualities[i].innerHTML;
        }
        diagrams[i].src = backsteps + "chords/" + chds_ft[mod(chds[base[i]] + trans, 12)].replace('♭', 'b') + qualities[i].innerHTML + ".svg";
    }

    /* Transpose Bass notes */

    for (var i = 0; i < bass_notes.length; i++) {
        if (accidental) {
            bass_elements[i].innerHTML = chds_ft[mod(chds[bass_notes[i]] + trans, 12)];
        } else {
            bass_elements[i].innerHTML = chds_sp[mod(chds[bass_notes[i]] + trans, 12)];
        }
    }

    /* Change Transpose number */
    if (capo) { output.innerHTML = -trans; }
    else { output.innerHTML = sign(trans); }
}

function tpup() {
    if (capo) { trans = trans - 1; }
    else { trans = mod(trans + 1, 12); }
    transpose();
}

function tpdown() {
    if (capo) { if (trans < 0) { trans = trans + 1; } }
    else { trans = mod(trans - 1, 12); }
    transpose();
}

function tr_capo() {
    var output = document.getElementById("count");
    var capo_label = document.getElementById("tr-capo");
    capo = !capo;
    if (capo) {
        capo_label.innerHTML = "Cp";
        output.innerHTML = mod(12-trans,12);
    }
    else {
        capo_label.innerHTML = "Tp";
        output.innerHTML = sign(trans);
    }
}

function ft_sp() {
    var b_but = document.getElementById("b_but");
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

    for (var i = 0; i < bass_elements.length; i++) {
        if (bass_elements[i].innerHTML.length != 1) {
            bass_elements[i].innerHTML = btos[bass_elements[i].innerHTML]
        }
    }
}



function autoScroll() {
    var play_speed = document.getElementById("speed");
    window.scrollBy(0, play_speed.value);
}
let scroll = true;
function startInverval() {
    var play_speed = document.getElementById("speed");
    if (scroll) {
        play_but.innerHTML = '<span class="icon">&#x23f8;</span>'
        scrolldelay = setInterval(autoScroll, 250);
        play_speed.style.visibility = "visible";
        console.log(play_speed.value);
    }
    else {
        play_but.innerHTML = '<span class="icon">&#9654;</span>'
        clearInterval(scrolldelay);
        play_speed.style.visibility = "hidden";
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

const sharp_keys = ['G', 'D', 'A', 'E', 'B', 'Em', 'Bm', 'F#m', 'C#m'];

if (sharp_keys.includes(song_key)) {
    var b_but = document.getElementById("b_but");
    b_but.innerHTML = '<span class="icon">&sharp;</span>';
}