const venue = '東京公演';
const anktext = ' 配席アンケート'


//ページロード時に参照するファンクション
window.onload = function () {

    const venueformlabel = document.querySelector('.timeform')
    const venues = document.querySelectorAll('.venue')
    if (venues.length = 1) {
        venuetext =
            `
        <label for="timeform1">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform1' name='matinee' onclick=checkEvent(1)>
            ${venues[1]}
        </label>
        `
    }
    else if (venues.length = 2) {
        venuetext =
            `
        <label for="timeform1">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform1' name='matinee' onclick=checkEvent(1)>
            ${venues[1]}
        </label>
        <label for="timeform2">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform2' name='evening' onclick=checkEvent(2)>
            ${venues[2]}
        </label>
        `
    }
    else {
        venuetext = ''
    }

    venueformlabel.innerHTML = venuetext

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


//チケット種別の選択肢を作成するファンクションです
function ticketformfunc(formlabel, i) {
    const formname = 'ticket' + i;
    const values = ['FC先行販売', '一般先行販売', '一般2次先行', '追加販売', 'プレイガイド受付'];
    createRadioformfunc(formlabel, formname, values, i)
}
//座席種別の選択肢を作成するファンクションです
function sheetformfunc(formlabel, i) {

    const formname = 'sheet' + i;
    const values = ['一般席', '女性エリア席', 'カメコエリア席', '着席指定席'];
    createRadioformfunc(formlabel, formname, values,);
}
//階層の選択肢を作成するファンクションです:HallTypeModelから参照します
function floorformfunc(formlabel, i) {
    block = [];
    var blocks = document.querySelectorAll('.blocks')
    for (let b = 0; b < blocks.length; b++) {
        block[b] = blocks[b].value;
    }

    const formname = 'floor' + i;

    createfloorformfunc(formlabel, formname, block, i);

    floorbuttons = document.querySelectorAll(`.floor${i}`);

}
//階層の選択肢から座席位置の選択肢を生成します:SheetModelから参照します
function newpositionfunc(i, floor) {
    const floorObjs = document.querySelector(`.${floor}`).querySelectorAll('div')
    const numberform = document.querySelector(`#numberform${i}`)
    numberform.innerHTML = ''

    floorObjs.forEach(function (floorObj) {
        var valid = floorObj.querySelector('.valid').value
        var prename = floorObj.querySelector('.prename').value
        var postname = floorObj.querySelector('.postname').value
        sheetHTML = sheetvalfunc(valid, i)
        var position = `
        <div id="errorform${i}_4">
            <div style="font-size:1.5rem">
                ${prename} ${sheetHTML} ${postname} 
            </div>
        </div>`
        numberform.innerHTML += position
    })

}

//ラジオボタンを作成するファンクションです。
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

//階層選択用のラジオボタンを作成するファンクションです。
function createfloorformfunc(formlabel, formname, values, i) {

    type = 'radio';
    values.forEach(function (value) {
        id = `${formname}_${value}`;
        ticketformtext =
            `<div class="form-check">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                    id="${id}" value="${value}" onclick="newpositionfunc(${i},'${value}')">
                    ${value}
                </label>
            </div>`;
        formlabel.innerHTML += ticketformtext;
    });
};

//公演を選択した際にアコーディオンメニューを表示するファンクションです。
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

//小文字のアルファベットを入力した際に大文字に自動変換するファンクションです。
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

//全ての質問を回答しているか確認をするファンクションです。
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

//座席位置の入力規則を呼び出すファンクションです。
function sheetvalfunc(val, i) {

    //1桁のアルファベットで定義づけられたブロックで使用します
    const val_101 =
        ` <input pattern="[A-Za-z]{1}" class="col-3 block position"  id="block_r${i}"  name="block_r${i}" oninput="inputChange(${i})" placeholder="英字1文字"> `

    const val_102 =
        `<input pattern="[A-Za-z]{1}" class="col-3 block position"  id="block_r${i}" name="block_r${i}" oninput="inputChange(${i})" placeholder="英字1文字">
        <input type="number" min="1" max="99 class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字"> `

    const val_103 =
        `<input type="number" min="1" max="9" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字"> `

    const val_201 =
        ` <input type="number" min="1" max="99" class="col-3 number position" id="row${i}" name="row${i}" placeholder="半角数字">`

    const val_301 =
        `<input type="number" min="1" max="999" class="col-3 number position" id="number${i}" name="number${i}" placeholder="半角数字"> `


    if (val == 101) {
        text = val_101
    }
    else if (val == 102) {
        text = val_102
    }
    else if (val == 103) {
        text = val_103
    }
    else if (val == 201) {
        text = val_201
    }
    else if (val == 301) {
        text = val_301
    }
    else {
        text = '該当なし'
    }

    return text
}