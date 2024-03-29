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
    const values = ['FC先行販売', '一般先行販売', '一般2次先行', '追加販売', 'プレイガイド受付'];
    createRadioformfunc(formlabel, formname, values, i)
}

function sheetformfunc(formlabel, i) {

    const formname = 'sheet' + i;
    const values = ['一般席', '女性エリア席', 'カメコエリア席', '着席指定席'];
    createRadioformfunc(formlabel, formname, values,);
}

function floorformfunc(formlabel, i) {
    block = [];
    var blocks = document.querySelectorAll('.blocks')
    for (let b = 0; b < blocks.length; b++) {
        block[b] = blocks[b].value
    }

    const formname = 'floor' + i;

    createRadioformfunc(formlabel, formname, block,);

    floorbuttons = document.querySelectorAll(`.floor${i}`);
    floorbuttons.forEach(function (floorbutton) {
        floorbutton.setAttribute('onclick', `positionformfunc(${i})`);
    });
}


function positionformfunc(i) {
    console.log(i);
    const floor = document.querySelector(`#floor${i}_アリーナ席`);
    const numberform = document.querySelector(`#numberform${i}`);

    const position1 = `
        </div><div id="errorform${i}_4"></div>
        <div class="blockform">
            <input pattern="[A-Za-z]{1}" class="col-3 block position" id="block_r${i}" placeholder="英字1文字"  oninput="inputChange(${i})">
            <input type="number" min="1" max="30" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字">
        <b style="font-size:1.5rem">ブロック</b>      
        
        <div class="numberform">
            <input type="number" min="1" max="1000" class="col-3 number position" id="number${i}" name="number${i}"
            placeholder="半角数字">
        <b style="font-size:1.5rem">番</b>
        </div>
    `;

    const position2 = `
        <div id="errorform${i}_4"></div>
        <div class="blockform">
            <input pattern="[A-Na-n]{1}" class="col-3 block position" id="block_r${i}"  placeholder="英字1文字"  oninput="inputChange(${i})">
                <b style="font-size:1.5rem">ブロック</b>      
        </div>
        <div class="rowform">
        <input type="number" min="1" max="1000" class="col-3 number position" id="row${i}" name="row${i}" placeholder="半角数字">
            <b style="font-size:1.5rem">列</b>      
        </div>
        <div class="numberform">
            <input type="number" min="1" max="1000" class="col-3 number position" id="number${i}" name="number${i}" placeholder="半角数字">
            <b style="font-size:1.5rem">番</b>
        </div>
    `;
    if (floor) {
        if (floor.checked) {
            numberform.innerHTML = position1;
        }
        else {
            numberform.innerHTML = position2;
        }
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
                    id="${id}" value="${value}">
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
    const blocktext = document.querySelector(`#block_r${i}`);
    const largeblock = document.querySelector(`#largeblock_r${i}`);
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

    const errormsg1 = '参加公演にチェックを入れてください';


    if (!(matinee.checked || evening.checked)) {
        errorform1.innerHTML = errormsg1;
        return false;
    }

    if (matinee.checked) {
        form1 = formcheck(1);
        console.log(form1);
    }
    else {
        form1 = true;
    }
    if (evening.checked) {
        form2 = formcheck(2);
    }
    else {
        form2 = true;
        console.log(form2);
    }

    if (!form1 || !form2) {
        return false;
    }
    else {
        return true;
    }

}

function formcheck(i) {
    const errormsg2 = '入力してください';

    const tickets = document.querySelectorAll(`.ticket${i}`);
    const sheets = document.querySelectorAll(`.sheet${i}`);
    const floors = document.querySelectorAll(`.floor${i}`);
    const block_r = document.querySelector(`#block_r${i}`);
    const block_c = document.querySelector(`#block_c${i}`);
    const row = document.querySelector(`#row${i}`)

    const error1 = document.querySelector(`#errorform${i}_1`);
    const error2 = document.querySelector(`#errorform${i}_2`);
    const error3 = document.querySelector(`#errorform${i}_3`);
    const error4 = document.querySelector(`#errorform${i}_4`);

    var is_ticket = false;
    var is_sheet = false;
    var is_floor = false;
    var is_blockr = false;
    var is_blockc = false;
    var is_row = false;

    tickets.forEach(function (ticket) {
        if (ticket.checked) {
            is_ticket = true;
            error1.innerHTML = "";
        }
    });
    if (!is_ticket) {
        error1.innerHTML = errormsg2;
    }

    sheets.forEach(function (sheet) {
        if (sheet.checked) {
            is_sheet = true;
            error2.innerHTML = "";
        }
    });
    if (!is_sheet) {
        error2.innerHTML = errormsg2;
    }

    floors.forEach(function (floor) {
        if (floor.checked) {
            is_floor = true;
            error3.innerHTML = "";
        }
    });
    if (!is_floor) {
        error3.innerHTML = errormsg2;
    }

    if (!is_ticket || !is_sheet || !is_floor) {
        return false;
    }

    if (block_r.value != '') {
        is_blockr = true;
    }

    else {
        is_blockc = true;
    }

    if (row) {
        if (row.value != '') {
            is_row = true;
        }
    }
    else {
        is_row = true;
    }

    if (!is_blockr || !is_row) {
        error4.innerHTML = errormsg2;
        return false;
    }
    else {
        error4.innerHTML = "";
    }
    return true
}
