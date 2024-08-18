var updateBtns = document.getElementsByClassName('update-cart')

for (i=0; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var item_id = this.dataset.product
        var action = this.dataset.action
        console.log('item_id ',item_id,'action',action)
        console.log('user : ',user)
        if (user === "AnonymousUser"){
            console.log('user not login')
        } else {
            updateUserOrder(item_id,action)
        }
    })
}

function updateUserOrder(productId,action){
    console.log('user login, success add')
    var url = '/update_cart/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken ,
        },
        body: JSON.stringify({'item_id':item_id,'action':action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data',data)
        location.reload()
    })
}