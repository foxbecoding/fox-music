<template>
	<div class="d-flex flex-no-wrap musicplayer-controls-container" >
        <div>
            <span  class="song-time">{{CURRENT_TIME_STR}} / {{DURATION_STR}}</span>
            <v-tooltip top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="prevSong"
                        v-bind="attrs"
                        v-on="on"  
                        icon
                    >
                        <v-icon>mdi-skip-previous</v-icon>
                    </v-btn>
                </template>
                <span>Previous</span>
            </v-tooltip>
            <v-tooltip top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="play_pause"
                        v-bind="attrs"
                        v-on="on"  
                        icon
                    >
                        <v-icon v-if="IS_PAUSED">mdi-play</v-icon>
                        <v-icon v-else>mdi-pause</v-icon>
                    </v-btn>
                </template>
                <span>Play</span>
            </v-tooltip>
            <v-tooltip top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="nextSong"
                        v-bind="attrs"
                        v-on="on" 
                        icon
                    >
                        <v-icon>mdi-skip-next</v-icon>
                    </v-btn>
                </template>
                <span>Next</span>
            </v-tooltip>
            <v-tooltip top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="shuffle" 
                        v-bind="attrs"
                        v-on="on" 
                        icon
                    >
                        <v-icon :color="IS_SHUFFLED ? 'blue': ''">mdi-shuffle-variant</v-icon>
                    </v-btn>
                </template>
                <span>Shuffle</span>
            </v-tooltip>
            <v-tooltip top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="loop" 
                        v-bind="attrs"
                        v-on="on" 
                        icon
                    >
                        <v-icon :color="IS_LOOP ? 'blue': ''">mdi-repeat</v-icon>
                    </v-btn>
                </template>
                <span>Loop</span>
            </v-tooltip>
            <v-tooltip v-if="$vuetify.breakpoint.smAndUp" top :disabled="$vuetify.breakpoint.smAndDown">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        @click="mute"
                        v-bind="attrs"
                        v-on="on"  
                        icon
                    >
                        <v-icon v-if="!IS_MUTED">mdi-volume-high</v-icon>
                        <v-icon v-else>mdi-volume-off</v-icon>
                    </v-btn>
                </template>
                <span>Mute</span>
            </v-tooltip>  
        </div>
        <div >
            <v-slider
                v-if="$vuetify.breakpoint.smAndUp"
                class=" musicplayer-slider__volume"
                color="red darken-1"
                v-model="volume"
                @input="volumeSlider"
                :min="0"
                :max="100"
                :ticks="false"
                :disabled="IS_MUTED"
            />
        </div>
    </div>
</template>
<script lang="ts">
import { MusicPlayerState } from '~/store/MusicPlayer';
import {  
    computed, 
    ref,
    useStore, 
    defineComponent, 
} from '@nuxtjs/composition-api';

export default defineComponent({
	setup() {
        const store = useStore<MusicPlayerState>();
        const volume = ref<number>(100);

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
        const DURATION_STR = computed<string>(() => {
            return store.getters['MusicPlayer/durationStr']
        });
        const CURRENT_TIME_STR = computed<string>(() => {
            return store.getters['MusicPlayer/currentTimeStr']
        });
        const IS_MUTED = computed<boolean>(
            () => store.getters['MusicPlayer/isMuted']
        ); 

        //methods
        const loop = (): void => {
            store.dispatch('MusicPlayer/loop')
        };   

        const mute = (): void => {
            store.dispatch('MusicPlayer/mute')
        };

        const nextSong = (): void => {
            store.dispatch('MusicPlayer/nextSong')
        };

        const play_pause = (): void => {
            store.dispatch('MusicPlayer/play_pause')
        };

        const prevSong = (): void => {
            store.dispatch('MusicPlayer/prevSong')
        };    
        
        const shuffle = (): void => {
            store.dispatch('MusicPlayer/shuffle')
        };
    
        const volumeSlider = (e: number): void => { 
            store.dispatch('MusicPlayer/volume', e)
        };

		return {
            volume,
            DURATION_STR,
            CURRENT_TIME_STR,
            IS_LOOP,
            IS_MUTED,
            IS_PAUSED,
            IS_SHUFFLED,
            loop,
            mute,
            nextSong,
            play_pause,
            prevSong,
            shuffle,
            volumeSlider,
		};
	}
})
</script>
<style lang="scss" scoped>
.musicplayer-slider__volume{
    position: relative;
    top: 23px;
    width: 70px;
}

.musicplayer-controls-container{
    position: relative;
    height: 48px;
    .song-time{
        font-size: 0.67rem;
    }
    @media screen and (max-width: 960px) {
        .song-time{
            position: absolute;
            left: 50px;
            width: 100%;
            top: 0;
        }
    }
}
</style>
