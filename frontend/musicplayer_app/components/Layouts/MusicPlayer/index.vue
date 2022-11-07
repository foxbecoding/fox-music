<template>
	<div class="musicplayer-container">
        <layoutsMusicPlayerDesktop v-if="$vuetify.breakpoint.smAndUp" />
        <layoutsMusicPlayerMobile v-if="$vuetify.breakpoint.xsOnly" />
  </div>
</template>
<script lang="ts">
import Song from '~/utils/types/Songs';
import Artist from '~/utils/types/Artists';
import { MusicPlayerState } from '~/store/MusicPlayer';
import { 
    computed, 
    defineComponent, 
    useRoute,
    useStore,
    watch,
} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {   
        const route = useRoute();
        const store = useStore<MusicPlayerState>();

        //computed
        const AUDIO = computed(() => {
            return store.getters['MusicPlayer/audio']
        });
        const IS_SLIDING = computed<boolean>(
            () => store.getters['MusicPlayer/isSliding']
        );       
        const SONG = computed<Song>( 
            () => store.getters['MusicPlayer/song']
        );

        //watchers
        watch(SONG, () => {
            if(route.value.name === 'playing-_id'){ 
                let path: string = route.value.fullPath
                history.replaceState({urlPath: path},"",`/playing/${SONG.value.uniqid}`)
            }          
            audioLoadedEvents();
            audioTimeUpdateEvents();
            audioEndedEvents();
            setMediaSessionData();           
        });

        //methods
        const audioLoadedEvents = (): void => {
            AUDIO.value.addEventListener('loadeddata', () => {
                if (AUDIO.value.readyState >= 4) {
                    store.commit('MusicPlayer/duration', AUDIO.value.duration);  
                }   
            });
        };

        const audioEndedEvents = (): void => {
            AUDIO.value.addEventListener('ended', () => {        
                AUDIO.value.ended ? songEnded() : '';
            })
        };

        const audioTimeUpdateEvents = (): void => {
            AUDIO.value.addEventListener('timeupdate', () => {
                if (IS_SLIDING.value === false){
                    store.commit('MusicPlayer/currentTime', AUDIO.value.currentTime);
                }    
            })  
        };

        const removeEvtListeners = (): void => {
            AUDIO.value.removeEventListener('loadeddata')
            AUDIO.value.removeEventListener('ended')
            AUDIO.value.removeEventListener('timeupdate')
        };

        const setMediaSessionData = (): void => {
            setTimeout(() => {
                if('mediaSession' in navigator) {
                navigator.mediaSession.metadata = new MediaMetadata({
                    title: SONG.value.title,
                    artist: artistNameStr(),
                    album: 'music.foxbecoding.com',
                    artwork: [{src: `/assets/song_thumbnails/${SONG.value.thumbnail}`}]
                });
                navigator.mediaSession.setActionHandler('play', () => { play_pause(); });
                navigator.mediaSession.setActionHandler('pause', () => { play_pause(); });
                navigator.mediaSession.setActionHandler('previoustrack', () => { prevSong(); });
                navigator.mediaSession.setActionHandler('nexttrack', () => { nextSong(); });
            }   
            }, 300);  
        };

        const play_pause = (): void => {
            store.dispatch('MusicPlayer/play_pause')
        };

        const songEnded = (): void => {
            // removeEvtListeners()
            store.commit('MusicPlayer/isEnded', true as boolean);
            nextSong();
        };
    
        const nextSong = (): void => {
            // removeEvtListeners()
            store.dispatch('MusicPlayer/nextSong')
        };

        const prevSong = (): void => {
            store.dispatch('MusicPlayer/prevSong')
        };

        const artistNameStr = (): string => {
            let names: string[] = [];
            SONG.value.artists.forEach((artist: Artist) => {
                names.push(artist.name);
            });
            return names.join('/');
        };
        
		return {};
	}
})
</script>
<style>
.v-slider__track-container{
    cursor: pointer !important; 
}
.v-slider__thumb{
    cursor: pointer !important; 
}
.v-slider--horizontal{
    min-height: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}
</style>
<style scoped>
.musicplayer-container{
    position: -webkit-sticky;
    position: sticky;
    bottom: 0;
}
</style>
