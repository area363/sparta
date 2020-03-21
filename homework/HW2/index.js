function order() {
    // name order address telelphone의 값을 가져온다
    let name = $('#name').val();
    let order = $('#order').val();
    let address = $('#address').val();
    let telephone = $('#telephone').val();

    // 이름을 입력하지 않을 경우 alert
    if (name.length === 0) {
        alert("성함을 입력해주세요!");
        $('#name').focus();

        // 수량을 선택하지 않을 경우 alert    
    } else if (order.length !== 1) {
        alert("수량을 선택해주세요!");
        $('#order').focus();

        // 주소를 입력하지 않을 경우 alert
    } else if (address.length === 0) {
        alert("주소를 입력해주세요!");
        $('#address').focus();

        // 전화번호에 "-"이 없을경우 alert
    } else if (telephone.indexOf("-") === -1) {
        alert("올바른 전화번호를 입력해주세요! (ex. 000-0000-0000)");
        $('#telephone').focus();

        // 모든 정보가 입력됐을 경우 주문완료 표시 & 밑섹션에 명단 추가
    } else {
        alert("주문완료!");
        make_card(name, order, address, telephone);
    }

}

function make_card(name, order, address, telephone) {

    // name, order, address, telephone값을 받아와 테이블 형식에 맞춰서 temp_html에 저장
    let temp_html = '<tr>\
        <td>'+ name + '</td>\
        <td>'+ order + '</td>\
        <td>'+ address + '</td>\
        <td>'+ telephone + '</td>\
        </tr>';

    // temp_html을 order-box에 추가
    $('#orders-box').append(temp_html);
}

