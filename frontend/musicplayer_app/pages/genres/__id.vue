<template>
    <div v-if="!$fetchState.pending">
        <v-container class="px-4 pb-0" fluid>
			<h2>{{genre.name}}</h2>
		</v-container>
        <SongsList :songs="songs" :title="`${songs.length} Songs`"/>
    </div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Song from '~/utils/types/Songs';
import Genre from '~/utils/types/Genres';
import { defineComponent, ref, shallowRef, useFetch, useRoute} from '@nuxtjs/composition-api';

export default defineComponent({
    setup() {
        const route = useRoute();
        const genre = ref<Genre>({} as Genre);
        const songs = shallowRef<Song[]>([]);
        useFetch(async () => {
            const genre_id = route.value.params._id
			let data = await $axios.$get(`${process.env.genresAPI+genre_id}`);
            genre.value = data;
            songs.value = data.songs;
		});
        return {
            genre,
            songs,
        };
    },
})
</script>
