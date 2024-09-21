//ページロード時に参照するファンクション
window.onload = function () {

    const $venueformlabel = $('.timeform')
    const venues = document.querySelectorAll('.venue')
    const venue_nam = ['matinee', 'evening']

    for (let i = 0; i < venues.length; i++) {
        venuetext =
            `
            <div class="form-check">
                <label>
                <input type='checkbox' class='form-check-input venue' id='timeform${i + 1}' name='venueform' onclick=checkEvent(${i})>
                ${venues[i].value}</label>
            </div>
        `;
        $venueformlabel.append(venuetext);
    };




}

function initializecheckbox() {
    var $formarea = $(`.formarea`);
    for (let i = 0; i < $formarea.length; i++) {
        if ($formarea.eq(i).find('div').length == 1 && $formarea.eq(i).find('input[type=radio]').length > 0) {
            $formarea.eq(i).find('input').click();
        }
    }
}

//公演を選択した際にアコーディオンメニューを表示するファンクションです。
function checkEvent(checkno) {
    const $timeform = $(`.timeform > div`).find('input');
    const $answerform = $('.answerform');

    if ($timeform.length == 3) {
        if (checkno == 2) {
            $timeform[0].checked = false;
            $timeform[1].checked = false;
        } else {
            $timeform[2].checked = false;
        }
    }


    for (i = 0; i < $timeform.length; i++) {
        if ($timeform[i].checked) {
            $answerform[i].classList.add('is-show');

        } else {
            $answerform[i].classList.remove('is-show');
        };
    }
    initializecheckbox();
};

//販売区分に応じたチケット区分に変化させるファンクション
//input1:object
//input2:time
//output:void
function changeTicketSelect($this) {
    const type = 'radio';
    var time = $this.getAttribute('form-num')

    var sale = $this.getAttribute('content')
    var $tickets = $(`#ticketTypeInput > .${sale} > input`);
    var formname = 'ticket' + time;

    var $form2 = $(`#formtitle${time}_2`)
    var $ticketformlabel = $(`#ticketform${time}`);
    var $sheetformlabel = $(`#sheetform${time}`);

    $form2.empty();
    $ticketformlabel.empty();
    $sheetformlabel.empty();

    $ticketformtitle =
        `
        <div class="formtitle">
            <h3>チケットの種類</h3>
        </div>
    `;

    $form2.prepend($ticketformtitle);

    for (var i = 0; i < $tickets.length; i++) {
        ticketval = $tickets[i].value;
        tickettype = $tickets[i].getAttribute('content');

        id = `${formname}_${ticketval}`;


        $ticketformtext =
            `
                <div class="form-check ${sale} my-2">
                    <label> 
                    <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                        id="${id}" value="${ticketval}" onclick="changeSheetSelect('${sale}','${tickettype}',${time})">
                    ${ticketval}
                    </label>
                </div>
            `;
        $ticketformlabel.append($ticketformtext);
    };

    if ($tickets.length == 1) {
        $(`#ticketform${time}`).find('input').click()
    }

}

function changesheet($this) {
    var formnum = $this.getAttribute('form-num');
    var ticket = $this.getAttribute('content');
    var $sheetforms = $(`#sheetform${formnum} > div`);

    for (i = 0; i < $sheetforms.length; i++) {
        if ($sheetforms[i].classList.contains('sheet_' + ticket)) {
            $sheetforms[i].classList.remove('display-none');
            if ($sheetforms.eq(i).find('input').length == 1) {
                $sheetforms.eq(i).find('input').prop('checked', true);
            }
        } else {
            $sheetforms[i].classList.add('display-none');
        };
    }
};


//チケット区分に応じた座席区分に変化させるファンクション
//input1:object
//input2:time
//output:void
function changeSheetSelect(salestype, tickettype, time) {
    const type = 'radio';
    var $sheets = $(`#ticketTypeInput > .${salestype} > .${tickettype} `).find(`input`);
    var formname = 'sheet' + time;

    var $form3 = $(`#formtitle${time}_3`)
    var $formlabel = $(`#sheetform${time}`);

    $form3.empty();
    $formlabel.empty();

    $sheetformtitle =
        `
        <div class="formtitle">
            <h3>座席の種類</h3>
        </div>
    `;

    $form3.prepend($sheetformtitle);

    for (var i = 0; i < $sheets.length; i++) {
        sheetval = $sheets[i].value;
        id = `${formname}_${sheetval}`;
        $ticketformtext =
            `
                <div class="form-check my-2">
                    <label>
                        <input class="form-check-input ${formname}" type="${type}" name="${formname}"
                        id="${id}" value="${sheetval}">
                        ${sheetval}
                    </label>
                </div>
            `;

        $formlabel.append($ticketformtext);
    };

    if ($sheets.length == 1) {
        $(`#sheetform${time}`).find('input').click()
    }
}
//階層区分に応じた座席番号に変化させるファンクション
//input1:object
//input2:time
//output:void
function changefloorSelect($this) {
    var time = $this.getAttribute('form-num')
    var priority = $this.getAttribute('priority');
    var $sheets = $(`#sheetTypeInput > .fr${priority}`).find('div')

    var $form5 = $(`#formtitle${time}_5`)
    var $inpForm = $(`#numberform${time}`);

    $form5.empty();
    $inpForm.empty();

    const $numberformtitle =
        `
        <div class="formtitle">
            <h3>配席位置</h3>
        </div>
         `;

    $form5.prepend($numberformtitle);

    for (var i = 0; i < $sheets.length; i++) {
        var $sheet = $sheets[i]
        var valid = $sheet.querySelector('.valid').value
        var prename = $sheet.querySelector('.prename').value
        var postname = $sheet.querySelector('.postname').value
        var $sheetHTML = sheetvalfunc(valid, time)
        var $position =
            `
            <div style="font-size:1.5rem">
                ${prename} ${$sheetHTML} ${postname} 
            </div>
        `
        $inpForm.append($position);
    };

    return;
};





//小文字のアルファベットを入力した際に大文字に自動変換するファンクションです。
function inputChange(i) {
    var $inp = document.querySelector(`#block_r${i}`);
    var text = $inp.value;

    if (text.match(/^[a-z]*$/)) {
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
    const allday = document.querySelector('#timeform3');

    const errorform1 = document.querySelector("#errorform1");
    const errormsg1 = '参加公演にチェックを入れてください';

    var is_matinee = true; //公演が存在しないかチェックが入っていればtrue
    var is_evening = true;
    var is_allday = true;

    var form1 = true; //公演ごとの回答項目がすべて入力されていればtrue
    var form2 = true;
    var form3 = true;



    if (matinee) { //公演が存在しなければそのままtrue、存在すればチェックの有ならフォームチェックに進む
        is_matinee = matinee.checked;
        if (is_matinee) {
            form1 = formcheck(1);
        } else {
            form1 = true;
        }
    }

    if (evening) {
        is_evening = evening.checked;
        if (is_evening) {
            form2 = formcheck(2);
        } else {
            form2 = true;
        }
    }

    if (allday) {
        is_allday = allday.checked;
        if (is_allday) {
            form3 = formcheck(3);
        } else {
            form3 = true;
        }
    }

    if (is_matinee == false && is_evening == false && is_allday == false) { //どちらか一方でも公演が存在してチェックしてないとfalse
        errorform1.innerHTML = errormsg1;
        return false;
    }


    if (form1 == false || form2 == false || form3 == false) {
        return false;
    }

    return true;
}

//全ての質問を回答しているか確認をするファンクションです。
function formcheck(formnum) {
    const errormsg2 = '入力してください';

    var is_sales = $(`#salesform${formnum} input:checked`).length;
    var is_ticket = $(`#ticketform${formnum} input:checked`).length;
    var is_sheets = $(`#sheetform${formnum} input:checked`).length;
    var is_floors = $(`#floorform${formnum} input:checked`).length;
    var $numberform = $(`#numberform${formnum} input`)

    var is_numbers = true;


    const error1 = $(`#errorform${formnum}_1`);
    const error2 = $(`#errorform${formnum}_2`);
    const error3 = $(`#errorform${formnum}_3`);
    const error4 = $(`#errorform${formnum}_4`);
    const error5 = $(`#errorform${formnum}_5`);

    error1.empty();
    error2.empty();
    error3.empty();
    error4.empty();
    error5.empty();

    for (let i = 0; i < $numberform.length; i++) {
        if ($numberform[i].value == "") {
            is_numbers = false;
        }
    }


    if (is_sales != 1) {
        error1.prepend(errormsg2);
    }

    if (is_ticket != 1) {
        error2.prepend(errormsg2);
    }

    if (is_sheets != 1) {
        error3.prepend(errormsg2);
    }

    if (is_floors != 1) {
        error4.prepend(errormsg2);
    }

    if (!is_numbers) {
        error5.prepend(errormsg2);
    }




    if (is_sales == 1 && is_ticket == 1 && is_sheets == 1 && is_floors == 1 && is_numbers == true) {
        submit_values(formnum);
        return true;
    } else {
        return false;
    }

}

function submit_values(formnum) {
    const venue_list = ['matinee', 'evening'];
    const inp_sale = $(`#form${formnum}_1`).find('input:checked').val();
    const inp_ticket = $(`#form${formnum}_2`).find('input:checked').val();
    const inp_sheet = $(`#form${formnum}_3`).find('input:checked').val();
    const inp_floor = $(`#form${formnum}_4`).find('input:checked').val();
    const inp_row = $(`#row${formnum}`).val() || '';
    const inp_block_c = $(`#block_c${formnum}`).val() || '';
    const inp_block_r = $(`#block_r${formnum}`).val() || '';
    const inp_number = $(`#number${formnum}`).val();

    const inp_venue = document.querySelector(`#timeform${formnum}`).checked;




    for (let a = 1; a < 4; a++) { //登録値を初期化する
        for (let b = 1; b < 9; b++) {
            $(`#sumbit_${a}_${b}`).val('');
        }
    }

    if (formnum == 3) {
        for (let i = 1; i < 3; i++) {
            $(`#submit_${i}_1`).val(inp_sale);
            $(`#submit_${i}_2`).val(inp_ticket);
            $(`#submit_${i}_3`).val(inp_sheet);
            $(`#submit_${i}_4`).val(inp_floor);
            $(`#submit_${i}_5`).val(inp_row);
            $(`#submit_${i}_6`).val(inp_block_c);
            $(`#submit_${i}_7`).val(inp_block_r);
            $(`#submit_${i}_8`).val(inp_number);
            $(`#sumbit_${venue_list[formnum - 1]}`).val('true');
        }
    } else {
        $(`#submit_${formnum}_1`).val(inp_sale);
        $(`#submit_${formnum}_2`).val(inp_ticket);
        $(`#submit_${formnum}_3`).val(inp_sheet);
        $(`#submit_${formnum}_4`).val(inp_floor);
        $(`#submit_${formnum}_5`).val(inp_row);
        $(`#submit_${formnum}_6`).val(inp_block_c);
        $(`#submit_${formnum}_7`).val(inp_block_r);
        $(`#submit_${formnum}_8`).val(inp_number);
        $(`#sumbit_${venue_list[formnum - 1]}`).val(inp_venue);
    }
}

//座席位置の入力規則を呼び出すファンクションです。
function sheetvalfunc(val, i) {

    //1桁のアルファベットで定義づけられたブロックで使用します

    const val_101 =
        ` <input pattern="[A-Za-z]{1}" class="col-3 block position"  id="block_r${i}"   oninput="inputChange(${i})" placeholder="英字1文字"> `

    const val_102 =
        `<input pattern="[A-Za-z]{1}" class="col-3 block position"  id="block_r${i}" oninput="inputChange(${i})" placeholder="英字1文字">
        <input type="number" min="1" max="99" class="col-3 number position" id="block_c${i}" placeholder="半角数字"> `

    const val_103 =
        `<input type="number" min="1" max="9" class="col-3 number position" id="block_c${i}" placeholder="半角数字"> `

    const val_201 =
        ` <input type="number" min="1" max="99" class="col-3 number position" id="row${i}"placeholder="半角数字">`

    const val_301 =
        `<input type="number" min="1" max="999" class="col-3 number position" id="number${i}"  placeholder="半角数字"> `

    //横アリスタンド用
    const val_1002 =
        `<select id="block_r${i}" class="col-3 block postion">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
        <option value="D">D</option>
        <option value="E">E</option>
        <option value="F">F</option>
    </select><input type="number" min="1" max="99" class="col-3 number position" id="row${i}"  placeholder="半角数字"> `

    const val_1003 =
        `<select id="block_r${i}" class="col-3 block postion">
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
