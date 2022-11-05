<template>
	<div v-if="!$fetchState.pending">
		<ArtistsList :artists="artists" title="Artists"/>
	</div>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Artist from '~/utils/types/Artists';
import { defineComponent, shallowRef, useFetch} from '@nuxtjs/composition-api';

export default defineComponent({
	setup() {
		const artists = shallowRef<Artist[]>([])
		useFetch(async () => {
			artists.value = await $axios.$get('/api/artists/') ;
		})
		return {
			artists,
		};
	},
})
</script>
