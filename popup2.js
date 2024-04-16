document.querySelector('#summaryform').addEventListener('submit',(e)=>{
    e.preventDefault();
    const inputText = document.getElementById('giventext').value;
    const data = { "url": inputText };
    document.querySelector('.logotext').innerHTML="Summarizing...";
    document.querySelector('.logo').classList.add('animation');
    fetch('http://localhost:5000/utubesummary',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then((res)=>{
        return res.text()}).then((data)=>{
            document.querySelector('html').style.height='500px';
            document.querySelector('.showsummary').innerHTML=data;
            document.querySelector('.logotext').innerHTML="Summarizer";
            document.querySelector('.logo').classList.remove('animation');
        })
})
document.querySelector('.menu').addEventListener('click',()=>{
    let items=document.querySelector('.menu_items');
    if(items.style.display==='none'){
        items.style.display='flex';
    }
    else{
        items.style.display='none';
    }
})