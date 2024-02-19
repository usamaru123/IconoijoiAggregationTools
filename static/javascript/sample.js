const venue = '東京公演';
const anktext = ' 配席アンケート'

window.onload = function () {

    for (let i = 0; i < 2; i++) {
        const ticketformlabel = document.querySelectorAll('.ticketform')[i];
        const sheetformlabel = document.querySelectorAll('.sheetform')[i];
        const floorformlabel = document.querySelectorAll('.floorform')[i];

        num = i + 1;
        ticketformfunc(ticketformlabel, num);
        sheetformfunc(sheetformlabel, num);
        floorformfunc(floorformlabel, num);
    }


}


function ticketformfunc(formlabel, i) {
    const formname = 'ticket' + i;
    const values = ['FC先行販売', '一般先行販売', '追加販売'];
    createRadioformfunc(formlabel, formname, values, i)
}

function sheetformfunc(formlabel, i) {
    const formname = 'sheet' + i;
    const values = ['一般席', '女性エリア席', 'カメコエリア席', '着席指定席'];
    createRadioformfunc(formlabel, formname, values,);
}

function floorformfunc(formlabel, i) {
    const formname = 'floor' + i;
    const values = ['アリーナ', '3階席', '4階席'];
    createRadioformfunc(formlabel, formname, values, i);

    floorbuttons = document.querySelectorAll(`.floor${i}`);
    floorbuttons.forEach(function (floorbutton) {
        floorbutton.setAttribute('onclick', `positionformfunc(${i})`);
    });
}


function positionformfunc(i) {
    console.log(i);
    const floor = document.querySelector(`#floor${i}_アリーナ`);
    const numberform = document.querySelector(`#numberform${i}`);

    const position1 = `
        <div class="blockform">
            <input pattern="[A-Za-z]{1}" class="col-3 block position" id="block${i}" placeholder="英字1文字"  oninput="inputChange(${i})">
            <input type="number" min="1" max="10" class="col-3 number position" id="number${i}" name="number${i}" placeholder="半角数字">
        <b style="font-size:1.5rem">ブロック</b>      


    </div>
        <div class="numberform">
            <input type="number" min="1" max="1000" class="col-3 number position" id="number${i}" name="number${i}"
            placeholder="半角数字">
        <b style="font-size:1.5rem">番</b>
        </div>
    `;

    const position2 = `
        <div class="blockform">
            <input pattern="[A-Za-z]{1}" class="col-3 block position" id="block${i}" placeholder="英字1文字"  oninput="inputChange()">
            <b style="font-size:1.5rem">ブロック</b>      
        </div>
        <div class="numberform">
            <input type="number" min="1" max="1000" class="col-3 number position" id="number${i}" name="number${i}" placeholder="半角数字">
            <b style="font-size:1.5rem">番</b>
        </div>
    `;

    if (floor.checked)
        numberform.innerHTML = position1;
    else {
        numberform.innerHTML = position2;
    }

};


function createRadioformfunc(formlabel, formname, values) {

    type = 'radio';
    values.forEach(function (value) {
        id = `${formname}_${value}`;
        ticketformtext =
            `<div class="form-check">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                    id="${id}" value="${value}" >
                    ${value}
                </label>
            </div>`;
        formlabel.innerHTML += ticketformtext;
    });
};

function checkEvent(num) {
    const timeform = document.querySelector(`#timeform${num}`);
    const answerform = document.querySelector(`#answerform${num}`);
    const timeformcheck = document.querySelector(`#timeformcheck${num}`)

    if (timeform.checked) {
        answerform.classList.add('is-show');
        timeformcheck.value = 'true'
    } else {
        answerform.classList.remove('is-show');
        timeformcheck.value = 'false'
    };
};

function inputChange(i) {
    const blocktext = document.querySelector(`#block${i}`);
    const largeblock = document.querySelector(`#largeblock${i}`);
    const largeblocktext = blocktext.value.toUpperCase();

    largeblock.value = largeblocktext;
};

function positionform_change(num) {
    const positionformlabel = document.querySelectorAll('.positionform')[num];
    positionformfunc(positionformlabel, num);
};

function valueCheck() {
    const matinee = document.querySelector('#timeform1');
    const evening = document.querySelector('#timeform2');
    const errorform1 = document.querySelector("#errorform1");
    const errorform2 = document.querySelector(".errorform");

    const errormsg1 = '参加公演にチェックを入れてください';
    const errormsg2 = '入力してください';

    if (!(matinee.checked || evening.checked)) {
        errorform1.innerHTML = errormsg1
        return false;
    }

    const ticket1 = document.querySelector('.ticket1')
    let flag = false;

    ticket1.forEach(function (ticket1) {
        if (ticket1.checked) {
            flag = true;
            console.log(flag)
        }
    })
    if (!flag) {
        errorform2.innerHTML = errormsg2
        return false;
    }
}

