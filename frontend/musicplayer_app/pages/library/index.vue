<template>
	<div v-if="!$fetchState.pending">
		<v-container class="px-4" fluid><h1>Library</h1></v-container>
		<LibrarySongsList
			@refresh="$fetch" 
			:songs="songs" 
			:artists="artists" 
			:genres="genres"
		/>
        <LibraryArtistsList @refresh="$fetch" :artists="artists"/>
        <LibraryGenresList @refresh="$fetch" :genres="genres"/>
		</div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Song from '~/utils/types/Songs';
import Genre from '~/utils/types/Genres';
import Artist from '~/utils/types/Artists';
import { defineComponent, shallowRef, useFetch} from '@nuxtjs/composition-api';

export default defineComponent({
    middleware: 'authenticated',
	setup() {
		const songs = shallowRef<Song[]>([]);
		const genres = shallowRef<Genre[]>([]);
		const artists = shallowRef<Artist[]>([]);
		
		useFetch(async () => {
			songs.value = await $axios.$get(`${process.env.songsAPI}`);
			genres.value = await $axios.$get(`${process.env.genresAPI}`);
			artists.value = await $axios.$get(`${process.env.artistsAPI}`);
		});
		return {
            songs,
            genres, 
            artists
        };
	},
})
</script>
