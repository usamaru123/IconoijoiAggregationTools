//ページロード時に参照するファンクション
window.onload = function () {

    const venueformlabel = document.querySelector('.timeform')
    const venues = document.querySelectorAll('.venue')
    if (venues.length == 1) {
        venuetext =
            `
        <label for="timeform1">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform1' name='matinee' onclick=checkEvent(1) checked>
            ${venues[0].value}
        </label>
        `
    }
    else if (venues.length == 2) {
        venuetext =
            `
        <label for="timeform1">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform1' name='matinee' onclick=checkEvent(1)>
            ${venues[0].value}
        </label>
        <label for="timeform2">
            <input type='checkbox' class='form-check-input' class='venue' id='timeform2' name='evening' onclick=checkEvent(2)>
            ${venues[1].value}
        </label>
        `
    }
    else {
        venuetext = ''
    }

    venueformlabel.innerHTML = venuetext

    //画面初期化
    checkEvent(1);
    $('#ticket1_FC先行').click();


}
//販売区分に応じたチケット区分に変化させるファンクション
//input1:object
//input2:time
//output:void
function changeTicketSelect($this, time) {
    const type = 'radio';

    var sale = $this.getAttribute('content')
    var $tickets = $(`#ticketTypeInput > .${sale} > input`);
    var formname = 'sheet' + time;
    var $formlabel = $(`#ticketform${time}`);

    $formlabel.empty();


    for (var i = 0; i < $tickets.length; i++) {
        ticketval = $tickets[i].value;
        tickettype = $tickets[i].attr('class');

        id = `${formname}_${ticketval}`;
        $ticketformtext =
            `<div class="form-check ${sale}">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                    id="${id}" value="${ticketval}" onclick="changeSheetSelect('${sale}',${tickettype},${time})">
                    ${ticketval}
                </label>
            </div>`;
        $formlabel.append($ticketformtext);
    };

    return;
}



//チケット区分に応じた座席区分に変化させるファンクション
//input1:object
//input2:time
//output:void
function changeSheetSelect(sale, $this, time) {
    const type = 'radio';
    var $sheets = $(`#ticketTypeInput > .${ticket} > .${sale} `).find(`input`);
    var formname = sale + time;
    var $formlabel = $(`#sheetform${time}`);

    $formlabel.empty();


    for (var i = 0; i < $sheets.length; i++) {
        sheetval = $sheets[i].value;
        id = `${formname}_${sheetval}`;
        $ticketformtext =
            `<div class="form-check">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                    id="${id}" value="${sheetval}">
                    ${sheetval}
                </label>
            </div>`;

        $formlabel.append($ticketformtext);
    };

    return;
}
//階層区分に応じた座席番号に変化させるファンクション
//input1:object
//input2:time
//output:void
function changefloorSelect($this, time) {

    var priority = $this.getAttribute('priority');
    var $sheets = $(`#sheetTypeInput > .fr${priority}`).find('div')
    var $inpForm = $(`#numberform${time}`);

    $inpForm.empty();

    for (var i = 0; i < $sheets.length; i++) {
        var $sheet = $sheets[i]
        var valid = $sheet.querySelector('.valid').value
        var prename = $sheet.querySelector('.prename').value
        var postname = $sheet.querySelector('.postname').value
        var $sheetHTML = sheetvalfunc(valid, time)
        var $position = `
        <div style="font-size:1.5rem">
            ${prename} ${$sheetHTML} ${postname} 
        </div>
       `
        $inpForm.append($position);
    };

    return;
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
    var $inp = document.querySelector(`#block_r${i}`);
    var text = $inp.value;

    if ($inp.match(/^[a-z]*$/)) {
        largetext = text.toUpperCase();
        $inp.value = largetext;
    }

    return;
};


function positionform_change(num) {
    const positionformlabel = document.querySelectorAll('.positionform')[num];
    positionformfunc(positionformlabel, num);

    return;
};


function valueCheck() {
    const matinee = document.querySelector('#timeform1');
    const evening = document.querySelector('#timeform2');
    const errorform1 = document.querySelector("#errorform1");

    const errormsg1 = '参加公演にチェックを入れてください';

    var is_matinee = true; //公演が存在しないかチェックが入っていればtrue
    var is_evening = true;

    var form1 = true; //公演ごとの回答項目がすべて入力されていればtrue
    var form2 = true;



    if (matinee) { //公演が存在しなければそのままtrue、存在すればチェックの有ならフォームチェックに進む
        is_matinee = matinee.checked;
        if (is_matinee) {
            form1 = formcheck(1);
        }
        else {
            form1 = true;
        }
    }

    if (evening) {
        is_evening = evening.checked;
        if (is_evening) {
            form2 = formcheck(2);
        }
        else {
            form2 = true;
        }
    }

    if (is_matinee == false && is_evening == false) { //どちらか一方でも公演が存在してチェックしてないとfalse
        errorform1.innerHTML = errormsg1;
        return false;
    }


    if (form1 == false || form2 == false) {
        return false;
    }

    return true;
}

//全ての質問を回答しているか確認をするファンクションです。
function formcheck(i) {
    const errormsg2 = '入力してください';

    const tickets = document.querySelectorAll(`.ticketform${i}`);
    const sheets = document.querySelectorAll(`.sheetform${i}`);
    const floors = document.querySelectorAll(`.floorform${i}`);
    const block_r = document.querySelector(`#block_r${i}`);
    const block_c = document.querySelector(`#block_c${i}`);
    const row = document.querySelector(`#row${i}`)
    const number = document.querySelector(`#number${i}`)

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
    var is_number = false;

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

    if (block_r) {
        if (block_r.value != '') {
            is_blockr = true;
        }
    }
    else {
        is_blockr = true;
    }


    if (row) {
        if (row.value != '') {
            is_row = true;
        }
    }
    else {
        is_row = true;
    }

    if (number) {
        if (number.value != '') {
            is_number = true;
        }
    }
    else {
        is_number = true;
    }

    if (!is_blockr || !is_row || !is_number) {
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
        <input type="number" min="1" max="99" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字"> `

    const val_103 =
        `<input type="number" min="1" max="9" class="col-3 number position" id="block_c${i}" name="block_c${i}" placeholder="半角数字"> `

    const val_201 =
        ` <input type="number" min="1" max="99" class="col-3 number position" id="row${i}" name="row${i}" placeholder="半角数字">`

    const val_301 =
        `<input type="number" min="1" max="999" class="col-3 number position" id="number${i}" name="number${i}" placeholder="半角数字"> `

    //横アリスタンド用
    const val_1002 =
        `<select id="block_r${i}" name="block_r${i}" class="col-3 block postion">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
        <option value="D">D</option>
        <option value="E">E</option>
        <option value="F">F</option>
    </select><input type="number" min="1" max="99" class="col-3 number position" id="row${i}" name="row${i}" placeholder="半角数字"> `

    const val_1003 =
        `<select id="block_r${i}" name="block_r${i}" class="col-3 block postion">
            <option value="東">東ブロック</option>
            <option value="西">西ブロック</option>
            <option value="南">南ブロック</option>
            <option value="北">北ブロック</option>
        </select>`

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
    else if (val == 1001) {
        text = val_1001
    }
    else if (val == 1002) {
        text = val_1002
    }
    else if (val == 1003) {
        text = val_1003
    }
    else {
        text = '該当なし'
    }

    return text
}

