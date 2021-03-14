<template>
<div class="container" style="display:flex">
    <!-- Chat Box UI -->
    <div class="row">
        <div class="col s12">
            <div class="card horizontal">
                <div id="chat-messages" class="card-content" v-html="chatContent">
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="input-field col s8">
            <input type="text" @keyup.enter="send">
        </div>
        <div class="input-field col s4">
            <button class="waves-effect waves-light btn">
                <i class="material-icons right">chat</i>
                Send
            </button>
        </div>
    </div>

    <!-- Active Users UI -->
    <!-- <div class="active_list">
       <div style="width:100px">
           <span>Icon</span>
           <span>UserName</span>
       </div>
       
    </div> -->
</div>
  
</template>

<script>
const io = require('socket.io-client');

export default {
    data(){
        return{
        ws: null, // Our websocket
        newMsg: '', // Holds new messages to be sent to the server
        chatContent: '', // A running list of chat messages displayed on the screen
        email: null, // Email address used for grabbing an avatar
        username: null, // Our username
        }
    },
    created(){
        var self = this;
    
        self.ws = io.connect('localhost:5000')

        // self.ws.emit('pingServer', 'PING!')
        
        self.ws.on('connect', function(){
            console.log("Reached Here")
            self.ws.emit('pingServer', {data:'PING!'})
        })
        
    },
    methods:{
    }

}
</script>

<style>

</style>