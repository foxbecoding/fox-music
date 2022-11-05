<template>
    <div v-if="song.title">
        <SongsDetails :song="song"/>
        <SongsList :songs="songs" title="Now playing"/>
    </div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Song from '~/utils/types/Songs';
import { MusicPlayerState } from '~/store/MusicPlayer';
import { 
    ref, 
    watch, 
    useRoute, 
    computed, 
    useStore,
    shallowRef, 
    onBeforeMount,
    defineComponent, 
} from '@nuxtjs/composition-api';

export default defineComponent({
    transition: 'slide',
    setup() {
        const route = useRoute();
        const store = useStore<MusicPlayerState>();
        const song = ref<Song>({} as Song);
        const songs = shallowRef<Song[]>([]);
        const SONG = computed<Song>( 
            () => store.getters['MusicPlayer/song']
        );
        const SONGS = computed<Song[]>( 
            () => store.getters['MusicPlayer/songs']
        );

        watch(SONG, () => {
            song.value = SONG.value
        });
        watch(SONGS, () => {
            songs.value = SONGS.value
        });
        onBeforeMount(() => {
            if(SONGS.value.length > 0){
                song.value = SONG.value
                songs.value = SONGS.value
            }else{
                getData()
            }
        })
        const getData = async (): Promise<void> => {
            const song_id = route.value.params._id
            if(SONGS.value.length == 0){
                song.value = await $axios.$get(`${process.env.songsAPI+song_id}/`);
			    songs.value = await $axios.$get(`${process.env.songsAPI}`);
                store.commit('MusicPlayer/isActive', true as boolean);
			    store.commit('MusicPlayer/song', song.value as Song);
			    store.commit('MusicPlayer/songs', songs.value as Song[]);
			    store.commit('MusicPlayer/songsConst', songs.value as Song[]);
			    store.commit('MusicPlayer/audio', `/assets/songs/${song.value.filename}` as string);
			    store.commit('MusicPlayer/isPaused', true);
            }
        }
        return {
            song,
            songs,
        };
    },
})
</script>
<style scoped>
.slide-enter-active, .slide-leave-active { 
    transition: transform .5s; 
}
.slide-enter, .slide-leave-active { 
    transform: translateY(100%);
}  

</style>
