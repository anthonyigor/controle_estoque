$(document).ready(function() {

    $('#id_estoque-0-produto').addClass('clProduto');
    $('#id_estoque-0-quantidade').addClass('clQuantidade');

    // desabilita primeiro campo saldo
    $('#id_estoque-0-saldo').prop("type", "hidden")

    // span para exibir saldo
    $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class="lead" style="padding-left: 10px;"></span>')

    //select2
    $('.clProduto').select2();

    // config botão add item
    $('#add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('#estoque').children().length;
        var tmplMarkup = $('#item-estoque').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#estoque').append(compiledTmpl);

        $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

        // desabilita o campo saldo
        $('#id_estoque-' + (count) + '-saldo').prop("type", "hidden")

        // span para exibir saldo
        $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px;"></span>')

        // animação para movimento de scroll ao adicionar item
        $('html, body').animate({
            scrollTop: $('#add-item').position().top - 200}, 800);

        $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
        $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');

        // span para exibir saldo
        $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px;"></span>')

        //select2
        $('.clProduto').select2();
    });
});

let estoque
let saldo
let campo
let campo2
let quantidade

$(document).on('change', '.clProduto', function() {
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

    $.ajax({
        url: url,
        type: 'GET',
        success: function(response) {
            estoque = response.data[0].estoque
            campo = self.attr('id').replace('produto', 'quantidade')
            $('#'+campo).val('')
        },
        error: function(xhr) {
        }
    })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    saldo = Number(estoque) - Number(quantidade);

    // atribui o saldo ao campo 'saldo'
    campo = $(this).attr('id').replace('quantidade', 'saldo')
    if (saldo < 0) {
        alert('O saldo não pode ficar negativo.')
        $('#'+campo).val(saldo)
        return
    }

    // desabilita o saldo
    $('#'+campo).prop("type", "hidden")

    $('#'+campo).val(saldo)

    // atribui o saldo ao campo 'saldo-span'
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
    $('#'+campo2).text(saldo)

});