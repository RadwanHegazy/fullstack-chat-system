

const socket_connection = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/connect/'
);


socket_connection.onmessage = function(e) {
    const data = JSON.parse(e.data);

    var user_id = data.user_id
    var status = data.status

    
    var box = document.getElementById(`${user_id}`);

    if (box){

        if (status == 'online'){
            box.classList.add('online')
        }else{
            box.classList.remove('online')
        }

    }

    
};

