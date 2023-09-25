
// record audio
var rec_btn = document.getElementById('start-record');
var stop_btn = document.getElementById('stop-record');
var form = document.querySelector('.voice-msg');
var list = document.querySelector('.voice-layer .list');
let chunks = []



function SendVoiceMessage (ajax_url){
    
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia){
    
        navigator.mediaDevices.getUserMedia({audio:true})
        .then(function(stream){
            const media_recorder = new MediaRecorder(stream);
            
            
            
            rec_btn.onclick = function(){
                console.log(media_recorder.state)
                media_recorder.start();
                rec_btn.style.display = 'none';
                stop_btn.style.display = 'block';
            }
            

            rec_btn.click()

            media_recorder.ondataavailable  = function(e){
                chunks.push(e.data)
            }
            
            stop_btn.onclick = function(){
                stop_btn.style.display = 'none';
                rec_btn.style.display = 'block';
                media_recorder.stop();
                // document.getElementById('send-v').classList.add('view')
                
            }
            
            
            media_recorder.onstop = function(e){
                let audio = document.createElement('audio');
                audio.setAttribute('controls','')
                audio.setAttribute('name','voice')
                let blob = new Blob(chunks,{ 'type' : 'audio/ogg; codecs=opus' });
                
                // ajax post
                var Data = new FormData();
                Data.append('audio',blob);
                Data.append('test','this is a test msg')
                Data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
                
                
                // $("#voice_msg").submit(function(e){
                //     e.preventDefault();
                //     $.ajax({
                //         url:"{% url 'voice_msg' user.username %}",
                //         type:"POST",
                //         data:Data,
                //         contentType:false,
                //         processData:false,
                //         cache:false,
                //         success:function(done){
                //             console.log("Data has been sent to the server !",done)
                //             window.location.href = "{% url 'done' %}";
                //         },
                //         error:function(error){
                //             console.log("Error",error)
                //         }
                //     })
                // })
    
    
    
    
    
                chunks = [];
                let ad_url = window.URL.createObjectURL(blob);
                audio.src = ad_url;
                list.innerHTML = '';
                
                let SendRecBtn = document.createElement('button')
                SendRecBtn.textContent = 'ارسال'
                


                list.append(audio);
                list.append(SendRecBtn);
                

                SendRecBtn.addEventListener('click',()=>{
                    
                    // write ajax function here
                    console.log('Send Ajax to : ', ajax_url)

                    document.querySelector('.voice-layer').classList.remove('view');
                })
                
    
    
    
    
    
    
    
            }
            
        })
    
        .catch(function(error){
            console.log('error',error)
        })
        
        
        
    }else {
        alert('There is an error with your browser')
    }
        
}