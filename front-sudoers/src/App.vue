<template>
  <v-app>
    <v-app-bar
      app
      color="blue-color"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <h1>
          Sudoers
        </h1>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://www.hackathoncastellon.com/#/"
        target="_blank"
        text
      >
        <span class="mr-2">hackathonfacsa</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
<style>
.blue-color{
  background-color:#004290 !important;
}
</style>
