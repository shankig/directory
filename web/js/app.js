var App = (function () {

    var BASE_URL = "/api/"
    
    //Would create response table
    var build_table = function (data) {
        $("table#search_table tbody").html("");
        
        if (data.length == 0) {
            $("table#search_table tbody").append('<tr><td colspan="10"><center>No Records found.</center></td></tr>');
        }
        
        $.each(data, function(index, value) {
            var data_str = "<tr>" +
                "<td>" + value['office_name'] + "</td>" +
                "<td>" + value['pincode'] + "</td>" +
                "<td>" + value['office_type'] + "</td>" +
                "<td>" + value['delivery_status'] + "</td>" +
                "<td>" + value['division_name'] + "</td>" +
                "<td>" + value['region_name'] + "</td>" +
                "<td>" + value['circle_name'] + "</td>" +
                "<td>" + value['taluk'] + "</td>" +
                "<td>" + value['district_name'] + "</td>" +
                "<td>" + value['state_name'] + "</td>" +
                "</tr>";        
            $("table#search_table tbody").append(data_str);
        });
    };

    //Search records 
    var search_record = function () {
        var request_data = {};
        
        $("input.search_field").each(function() {
            var value = $(this).val();
            
            if (value) {
                request_data[$(this).attr('name')] = value;
            }
        });
        
        if ($.isEmptyObject(request_data)) {
            return;
        }
        
        $.getJSON(BASE_URL, request_data, function(data) {
            build_table(data)
        });
    };

    return {
        "search_record": search_record
    };
})(App);

