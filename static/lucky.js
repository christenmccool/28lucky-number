function clearErrors() {
    $("#name-err").empty();
    $("#year-err").empty();
    $("#email-err").empty();
    $("#color-err").empty();
}

/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();

    clearErrors();    

    $("#lucky-results").empty();

    const name = $('#name').val();
    const year = $('#year').val();
    const email = $('#email').val();
    const color = $('#color').val();

    const response = await axios.post('/api/get-lucky-num', {name:name, year:year, email:email, color:color})

    handleResponse(response)
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    const data = resp.data

    if ("errors" in data) {
        $("#name-err").append(data.errors.name);
        $("#year-err").append(data.errors.year);
        $("#email-err").append(data.errors.email);
        $("#color-err").append(data.errors.color);
    } else {
        const html = `<p>Your lucky number is ${data.num.num}. ${data.num.fact}<p>
        <p>Your birth year (${data.year.year}) fact is ${data.year.fact}</p>`
        $('#lucky-results').append(html);

        // $('#lucky-form').trigger('reset');
    }
}


$("#lucky-form").on("submit", processForm);


