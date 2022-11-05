<template>
	<v-row class="px-6">
        <v-toolbar flat height="50" color="rgb(12,12,12)"> 
            <v-btn @click="shuffle" icon small>
                <v-icon :color="IS_SHUFFLED ? 'blue': ''">mdi-shuffle-variant</v-icon>
            </v-btn>
            <v-spacer />
            <v-btn @click="prevSong" icon small>
                <v-icon>mdi-skip-previous</v-icon>
            </v-btn>
            <v-spacer />
            <v-btn @click="play_pause" icon small>
                <v-icon v-if="IS_PAUSED">mdi-play</v-icon>
                <v-icon v-else>mdi-pause</v-icon>
            </v-btn>
            <v-spacer />
            <v-btn @click="nextSong" icon small>
                <v-icon>mdi-skip-next</v-icon>
            </v-btn>
            <v-spacer />
            <v-btn @click="loop" icon small>
                <v-icon :color="IS_LOOP ? 'blue': ''">mdi-repeat</v-icon>
            </v-btn>
        </v-toolbar>
    </v-row>
</template>
<script lang="ts">
import { MusicPlayerState } from '~/store/MusicPlayer';
import {  
    computed, 
    useStore, 
    defineComponent, 
} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {
        const store = useStore<MusicPlayerState>();

        //computed
        const IS_PAUSED = computed<boolean>(
            () => store.getters['MusicPlayer/isPaused']
        );  
        const IS_LOOP = computed<boolean>(
            () => store.getters['MusicPlayer/isLoop']
        );  
        const IS_SHUFFLED = computed<boolean>(
            () => store.getters['MusicPlayer/isShuffled']
        );      

        //methods
        const play_pause = (): void => {
            store.dispatch('MusicPlayer/play_pause')
        };

        const loop = (): void => {
            store.dispatch('MusicPlayer/loop')
        };

        const shuffle = (): void => {
            store.dispatch('MusicPlayer/shuffle')
        };

        const nextSong = (): void => {
            store.dispatch('MusicPlayer/nextSong')
        };

        const prevSong = (): void => {
            store.dispatch('MusicPlayer/prevSong')
        };     

		return {
            IS_LOOP,
            IS_PAUSED,
            IS_SHUFFLED,
            loop,
            shuffle,
            nextSong,
            prevSong,
            play_pause,
		};
	}
})
</script>

