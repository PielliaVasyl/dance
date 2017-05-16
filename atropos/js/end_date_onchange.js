$('document').ready( function(){
    document.getElementById('id_start_date').addEventListener('change', function () {
    var from = $("#id_start_date").val();
    var to = $("#id_end_date").val();

    if (Date.parse(from) > Date.parse(to)) {
        document.getElementById("id_end_date").value = $("#id_start_date").val();
    }
    });
});

