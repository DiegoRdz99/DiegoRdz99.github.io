const letterContainer = document.getElementById('letter-container');
const optionsContainer = document.getElementById('options-container');
const userInputSection = document.getElementById('user-input-section');
const newGameContainer = document.getElementById('new-game-container');
const newGameButton = document.getElementById('new-game-button');
const canvas = document.getElementById('canvas');
const resultText = document.getElementById('result-text');
const henkerBox = document.getElementById('henker-box');

// Optionen

let options = {
    Länder: ['Deutschland', 'Mexiko', 'Kolumbien', 'Kanada', 'Brasilien', 'Spanien', 'Argentinien', 'Österreich', 'Japan', 'China', 'England', 'Italien'],
    Farben: ['rot', 'gelb', 'blau', 'grau', 'grün', 'braun', 'lila', 'rosa'],
    Generell: ['heiße','bin','Jahren','alt','wer','wie','ist','bist','du','ich'],
    Zahlen: ['zwanzig','zehn','eins','drei','zwölf','elf','vier','fünf','sechs','sieben','acht','neun','zwei','zehn','einhundertfünfundsiebzig','sechsunddreißig','dreißig','vierzehn','siebzig','siebzehn','dreizehn']
}

let Charaktere = ['messi','isabel','elsa','peppa','cr7','mbappe','backyardigan','harry','chatnoir','ladybug','santa'];

//
let richtigZähler = 0;
let zähler = 0;
let zielWort = '';
let Person = '';

//
const displayOptions = () => {
    optionsContainer.innerHTML += `<h3>Bitte wählen Sie eine Option`;
    let buttonCon = document.createElement('div');
    for (let value in options) {
        buttonCon.innerHTML += `<button class="options" onclick="generateWord('${value}')">${value}</button>`;
    }
    optionsContainer.appendChild(buttonCon);
}

// Schaltfläche Blockieren

const blocker = () => {
    let optionsButtons = document.querySelectorAll('.options');
    let letterButtons = document.querySelectorAll('.letters');
    // Optionen deaktivieren
    optionsButtons.forEach(button => {
        button.disabled = true;
    });
    // Buchstaben deaktivieren
    letterButtons.forEach(button => {
        button.disabled.true
    });
    newGameContainer.classList.remove('hide');
}


// Wörtergenerator

const generateWord = (optionValue) => {
    let optionsButtons = document.querySelectorAll('.options');
    optionsButtons.forEach((button) => {
        if (button.innerText.toLowerCase() === optionValue.toLowerCase()) {
            button.classList.add('active');
        }
        else {
            button.disabled = true;
        }
    });

    // Buchstaben verstecken, vorheriges Wort löschen
    letterContainer.classList.remove('hide');
    userInputSection.innerText = '';

    let optionArray = options[optionValue];
    // zufälliges Zahl auswählen
    zielWort = optionArray[Math.floor(Math.random() * optionArray.length)];
    console.log(zielWort);

    // jede Buchstabe durch ein Span mit einem Unterstrich
    let displayItem = zielWort.replace(/./g, '<span class="dashes">-</span>');

    // jedes Element zeigen
    userInputSection.innerHTML = displayItem;
}

// load

const initializer = () => {
    henkerBox.classList.remove('blur');
    richtigZähler = 0;
    zähler = 0;

    // Anfangs alle Elemente löschen und die Buchstabenchaltflächen verstecken
    userInputSection.innerHTML = '';
    optionsContainer.innerHTML = '';
    letterContainer.classList.add('hide');
    newGameContainer.classList.add('hide');
    letterContainer.innerHTML = '';


    // Schaltfläche für die Buchstaben
    let Buchstaben = [];
    for (let i = 65; i < 91; i++) {
        Buchstaben.push(String.fromCharCode(i));
    }
    Buchstaben.push('Ä', 'Ö', 'Ü', 'ß');
    Buchstaben.forEach((Buchstabe) => {
        let button = document.createElement('button');
        button.classList.add('letters');
        // character click
        button.addEventListener('click', () => {
            let charArray = zielWort.split('');
            let dashes = document.getElementsByClassName('dashes');
            //falls das Array das geclicktes Buchstabe enthaltet, die dazugehörige Dashes durch diese Buchstabe ersetzen
            if (charArray.includes(button.innerText)) {
                charArray.forEach((char, index) => {
                    if (char === button.innerText) {
                        dashes[index].innerText = char;
                        // richtigZähler erhöhen
                        richtigZähler++;
                        if (richtigZähler == charArray.length) {
                            resultText.innerHTML = `<h2 class='win-msg'>Du hast gewonnen!!</h2><p>Das Wort war eigentlich <b>${zielWort}</b></p>`;

                            blocker();
                        }
                    }
                });
            }
            else {
                // Fehlerzähler
                zähler++;
                // Zeichnen
                drawMan(zähler);
                // Mit 6 Fehler wird es schon verloren (1 Kopf, 2 Körper, 3 rechter Arm, 4 linker Arm, 5 rechtes Bein, 6 linkes Bein)
                if (zähler == 6) {
                    resultText.innerHTML = `<h2 class='lose-msg'>Pech gehabt!</h2><p>Das Wort war eigentlich <b>${zielWort}</b></p>`;
                    henkerBox.classList.add('blur');
                    blocker();
                }
            }
            // Die Buchstabeschaltfläche deaktivieren
            button.disabled = true;

        });
        letterContainer.append(button);
        button.innerText = Buchstabe;
        letterContainer.append(button);
    });

    displayOptions();
    // Canvas Kreation
    let { initialDrawing } = canvasCreator();
    initialDrawing();
}

//Canvas
const canvasCreator = () => {
    let context = canvas.getContext('2d');
    context.beginPath();
    context.strokeStyle = '#000';
    context.lineWidth = 2;

    const drawLine = (fromX, fromY, toX, toY) => {
        context.moveTo(fromX, fromY);
        context.lineTo(toX, toY);
        context.stroke();
    };

    const head = () => {
        base_image = new Image();
        Person = Charaktere[Math.floor(Math.random() * Charaktere.length)];
        base_image.src = `Bilder/${Person}.png`;
        base_image.onload = function () {
            context.drawImage(base_image, 40, 15, 60, 60);
        }
        // context.beginPath();
        // context.arc(70, 30, 10, 0, Math.PI * 2, true);
        // context.stroke();
    };

    const body = () => {
        drawLine(70, 70, 70, 90);
    };

    const leftArm = () => {
        drawLine(70, 70, 50, 70);
    };

    const rightArm = () => {
        drawLine(70, 70, 90, 70);
    };

    const leftLeg = () => {
        drawLine(70, 90, 50, 100);
    };

    const rightLeg = () => {
        drawLine(70, 90, 90, 100);
    };

    const initialDrawing = () => {
        context.clearRect(0, 0, context.canvas.width, context.canvas.height);
        //bottom line
        drawLine(10, 130, 80, 130);
        drawLine(10, 10, 10, 130);
        drawLine(10, 10, 70, 10);
        drawLine(70, 10, 70, 20);
    };

    return { initialDrawing, head, body, leftArm, rightArm, leftLeg, rightLeg};
};

// Das Mann zeichnen

const drawMan = (zähler) => {
    let { head, body, leftArm, rightArm, leftLeg, rightLeg } = canvasCreator();
    switch (zähler) {
        case 1:
            head();
            break;
        case 2:
            body();
            break;
        case 3:
            leftArm();
            break;
        case 4:
            rightArm();
            break;
        case 5:
            leftLeg();
            break;
        case 6:
            rightLeg();
            break;
        default:
            break;
    }
}


// initial frame




// neues Spiel
newGameButton.addEventListener('click', initializer);
window.onload = initializer;

