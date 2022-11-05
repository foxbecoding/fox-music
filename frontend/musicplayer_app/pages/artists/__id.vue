<template>
    <div v-if="!$fetchState.pending">
        <ArtistsArtistDetails :artist="artist"/>
        <SongsList :songs="songs" :title="`${songs.length} Songs`"/>
    </div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Song from '~/utils/types/Songs';
import Artist from '~/utils/types/Artists';
import { defineComponent, ref, shallowRef, useFetch, useRoute} from '@nuxtjs/composition-api';

export default defineComponent({
    transition: 'slide',
    setup() {
        const route = useRoute();
        const artist = ref<Artist>();
        const songs = shallowRef<Song[]>([]);
        useFetch(async () => {
            const artist_id = route.value.params._id
			let data = await $axios.$get(`${process.env.artistsAPI+artist_id}`);
            artist.value = data;
            songs.value = data.songs;
		});
        return {
            artist,
            songs
        };
    },
})
</script>
<style scoped>
.slide-enter-active, .slide-leave-active { 
    transition: transform .5s; 
}
.slide-enter, .slide-leave-active { 
    transform: translateX(100%);
}  
</style>
