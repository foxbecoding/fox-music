<template>
  <v-app class="app" dark>
    <v-app-bar
      :clipped-left=true
	    color="rgb(3,3,3)"
      class="app-toolbar__content"
      fixed
      app
	    flat
    >
      <img @click="$router.push('/')" src="/assets/logo.png" width="125"/>
      <v-spacer />
      <v-btn
        v-for="(nav, i) in nav_btns"
        class="nav-btn__text"
        :key="i"
        :to="nav.to"
        plain
        :icon="$vuetify.breakpoint.xsOnly ? true : false"
      >
        <v-icon>{{nav.icon}}</v-icon>
        <span v-if="$vuetify.breakpoint.smAndUp">{{nav.title}}</span>
      </v-btn>
      <v-spacer />
      <v-btn v-if="!AUTH_TOKEN" outlined x-small color="blue" to="/auth">Sign in</v-btn>
      <v-btn v-else @click="$router.push('/library')" icon><v-icon>mdi-music-box-multiple</v-icon></v-btn>
    </v-app-bar>
    <v-main>
      <v-container class="px-0" fluid>
        <Nuxt />
      </v-container>
    </v-main>
    <LayoutsMusicPlayer  />
    <LayoutsSnackBar />
  </v-app>
</template>

<script lang="ts">
import { defineComponent, useStore, computed, ref} from '@nuxtjs/composition-api';

export default defineComponent({
  name: 'DefaultLayout',
  setup() {
    interface NavBtns {
      icon: string;
      title: string;
      to: string;
    };
    const nav_btns = ref<NavBtns[]>([
      {
        icon: 'mdi-home',
        title: 'Home',
        to: '/'
      },
      {
        icon: 'mdi-account-music',
        title: 'Artists',
        to: '/artists'
      }
    ]);
    const store = useStore();
      //computed
    const AUTH_TOKEN = computed(() => {
        return store.getters['auth_token'];
    })
    return {nav_btns, AUTH_TOKEN};
  }
})
</script>
<style scoped>
.app{
  background: rgb(3,3,3) !important;
}
.app-toolbar__content{
  border-bottom: thin solid rgba(255,255,255,0.12) !important;
}
.nav-btn__text {
  font-size: 1.25rem !important;
}
</style>