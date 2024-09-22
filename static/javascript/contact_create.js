function valueCheck() {
    const email_regex = /.+@.+\..+/;

    const email_error1 = '正しいメールの形式を入力してください';
    const contact_text_error1 = '質問内容は入力必須です';

    //const $nam = $('#name');
    const $email = document.querySelector('#email');
    const $contact_text = document.querySelector('#contact_text');

    const $email_error = document.querySelector('#error_2');
    const $contact_error = document.querySelector('#error_3');

    $email_error.innerHTML = '';
    $contact_error.innerHTML = '';

    //let ls_nam = false;
    let is_email = false;
    let is_contact_text = false;

    if ($email.value.match(email_regex) || $email.value == '') {
        is_email = true;
    } else {
        $email_error.prepend(email_error1);
    }

    if ($contact_text.value != '') {
        is_contact_text = true;
    } else {
        $contact_error.prepend(contact_text_error1)
    };

    if (is_email && is_contact_text) {
        return true;
    } else {
        return false;
    }
}