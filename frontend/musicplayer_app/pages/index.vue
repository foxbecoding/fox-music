<template>
	<div v-if="!$fetchState.pending">
		<ArtistsFeatureList :artists="artists" title="Featured Artists"/>
		<SongsList :songs="songs" title="Explore"/>
	</div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Song from '~/utils/types/Songs';
import Artist from '~/utils/types/Artists';
import { defineComponent, shallowRef, useFetch } from '@nuxtjs/composition-api';

export default defineComponent({
	setup() {
		const songs = shallowRef<Song[]>([]);
		const artists = shallowRef<Artist[]>([]);
		
		useFetch(async () => {
			songs.value = await $axios.$get(`${process.env.songsAPI}`);
			artists.value = await $axios.$get(`${process.env.artistsAPI}?limit=8`);
		})
		return {artists, songs};
	},
})
</script>
