const venue = '東京公演';
const anktext = ' 配席アンケート'

window.onload = function () {

    for (let i = 0; i < 2; i++) {
        const ticketformlabel = document.querySelectorAll('.ticketform')[i];
        const sheetformlabel = document.querySelectorAll('.sheetform')[i];
        const positionformlabel = document.querySelectorAll('.positionform')[i];

        num = i + 1;
        ticketformfunc(ticketformlabel, num);
        sheetformfunc(sheetformlabel, num);
        positionformfunc(positionformlabel, num);
    }


}


function ticketformfunc(formlabel, i) {
    const formname = 'ticket' + i;
    const values = ['FC先行販売', '一般先行販売', '追加販売'];
    createRadioformfunc(formlabel, formname, values, i)
}

function sheetformfunc(formlabel, i) {
    const formname = 'sheet' + i;
    const values = ['一般席', '女性エリア席', 'カメコエリア席', '着席指定席']
    createRadioformfunc(formlabel, formname, values,)
}

function positionformfunc(formlabel, i) {
    const formname = 'floor' + i;
    const values = ['アリーナ', '3階席', '4階席'];
    createRadioformfunc(formlabel, formname, values, i);

    const position = `
        <div class="blockform">
            <input pattern="[A-Za-z]{1}" class="col-4 block position" id="block${i}" placeholder="半角英字１文字"  oninput="inputChange()">
            <input type="number" min="1" max="10" class="col-4 number position" id="number${i}" name="number${i}" placeholder="半角数字">
        <b style="font-size:1.5rem"> ブロック</b>      

 
    <b style="font-size:1.5rem">番</b>
    </div>
        <div class="numberform">
            <input type="number" min="1" max="1000" class="col-5 number position" id="number${i}" name="number${i}"
            placeholder="半角数字">
        <b style="font-size:1.5rem">番</b>
        </div>
`
    formlabel.innerHTML += position;
}

function createRadioformfunc(formlabel, formname, values) {

    type = 'radio';
    values.forEach(function (value) {
        id = `${formname}_${value}`;
        ticketformtext =
            `<div class="form-check">
                    <label for="${id}" class="form-check-label">
                        <input class="form-check-input" type="${type}" class="form-control" name="${formname}"
                    id="${id}" value="${value}" >
                    ${value}
                </label>
            </div>`;
        formlabel.innerHTML += ticketformtext;
    });
}

function checkEvent1() {
    checkEvent(1);
};

function checkEvent2() {
    checkEvent(2);
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


function inputChange() {
    const blocktext1 = document.querySelector('#block1');
    const largeblock1 = document.querySelector('#largeblock1');
    const blocktext2 = document.querySelector('#block2');
    const largeblock2 = document.querySelector('#largeblock2');

    const largeblocktext1 = blocktext1.value.toUpperCase();
    const largeblocktext2 = blocktext2.value.toUpperCase();

    largeblock1.value = largeblocktext1;
    largeblock2.value = largeblocktext2;
}