<template>
	<div class="musicplayer-large" v-show="IS_ACTIVE" :app="IS_ACTIVE">
        <v-toolbar color="rgb(8,8,8)">
            <LayoutsMusicPlayerDesktopTimeSlider />
            <LayoutsMusicPlayerDesktopSongDetails />
            <v-spacer />
            <LayoutsMusicPlayerDesktopControls />
            <v-spacer />
            <v-btn 
                class="now-playing-btn"
                :to="$route.name != 'playing-_id' ? `/playing/${SONG.uniqid}` : '/'" 
                icon
            >
                <v-icon v-if="$route.name != 'playing-_id'">mdi-menu-up</v-icon>
                <v-icon v-else>mdi-menu-down</v-icon>
            </v-btn>
        </v-toolbar>
    </div>
</template>
<script lang="ts">
import { computed, defineComponent, useStore} from '@nuxtjs/composition-api';
import Song from '~/utils/types/Songs';
export default defineComponent({
	setup() {
        const store = useStore()

        //computed
        const IS_ACTIVE = computed<boolean>(
            () => store.getters['MusicPlayer/isActive']
        );     
        const SONG = computed<Song>( 
            () => store.getters['MusicPlayer/song']
        );

		return { 
            IS_ACTIVE,
            SONG
		};
	}
})
</script>
<style scoped>
musicplayer-large{
    width: 100%;
}
</style>

