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
        checkEvent(1)
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

    createfloorformfunc(formlabel, formname, block,);

    floorbuttons = document.querySelectorAll(`.floor${i}`);

}

function newpositionfunc(i) {
    const val_101 =
        ` <input pattern="[A-Za-z]{1}" class="col-3 block position" id="block_r${i}" placeholder="英字1文字"  oninput="inputChange(${i})">`

    const val_102 =
        `<input pattern="[A-Za-z]{1}" class="col-3 block position" id="block_r${i}" placeholder="英字1文字"  oninput="inputChange(${i})">`
}

function positionformfunc(i) {
    console.log(i);
    const floor_arena = document.querySelector(`#floor${i}_１階アリーナ席`);
    const floor_1 = document.querySelector(`#floor${i}_１階席`)
    const numberform = document.querySelector(`#numberform${i}`);

    const position1 = `
        </div><div id="errorform${i}_4"></div>
        <div class="blockform">
        GATE<input pattern="[A-Za-z]{1}" class="col-3 block position" id="block_r${i}" placeholder="英字1文字"  oninput="inputChange(${i})">
            <input type="number" min="1" max="30" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字">
    <b style="font-size:1.5rem">列</b>      
        
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

    const position3 = `
    </div><div id="errorform${i}_4"></div>
    <div class="blockform">
    <b style="font-size:1.5rem">GATE</b> 
    <input type="number" min="1" max="10" class="col-3 number position" id="block_r${i}" name="block_r${i}" placeholder="半角数字">
        <input type="number" min="1" max="99" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字">
<b style="font-size:1.5rem">列</b>      
    
    <div class="numberform">
        <input type="number" min="1" max="1000" class="col-3 number position" id="number${i}" name="number${i}"
        placeholder="半角数字">
    <b style="font-size:1.5rem">番</b>
    </div>
`;
    /* if (floor_) {
    if (floor_arena.checked) {
        numberform.innerHTML = position3;
    }
    else {
        numberform.innerHTML = position2;
    }
}
if (floor_1) {
    if (floor_1.checked) {
        numberform.innerHTML = position1;
    }
    else {
        numberform.innerHTML = position2;
    }
}
    */
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

function createfloorformfunc(formlabel, formname, values) {

    type = 'radio';
    values.forEach(function (value) {
        id = `${formname}_${value}`;
        ticketformtext =
            `<div class="form-check">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                    id="${id}" value="${value}" onclick="positionformfunc(${value})">
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



    if (matinee) {
        is_matinee = matinee.checked
        if (matinee.checked) {
            form1 = formcheck(1);
        }
        else {
            form1 = false;
        }
    }
    else {
        is_matinee = true
    }
    if (evening) {
        is_evening = evening.checked
        if (evening.checked) {
            form2 = formcheck(2);
        }
        else {
            form2 = false;
            console.log(form2);
        }
    }
    else {
        is_evening = true
    }

    if (!(is_matinee || is_evening)) {
        errorform1.innerHTML = errormsg1;
        return false;
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
