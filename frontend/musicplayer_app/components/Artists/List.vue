<template>
	<div>
		<v-container class="px-4 pb-0" fluid>
			<h2>{{title}}</h2>
		</v-container>
		<v-container class="px-4" fluid>
			<v-row >
				<v-col
					v-for="(artist, i) in artists" 
					:key="`artist_${i}`"
					cols="6"
					sm="4"
					md="2"
					lg="2"
				>
					<div 
						class="artist-content" 
						@click="$router.push(`/artists/${artist.uniqid}`)"
					>
						<v-img
							v-ripple 
							:src="`/assets/${artist.img_file_path}`" 
							class="artist-image"
						/>
						<p>{{artist.name}}</p>
					</div>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>
<script lang="ts">
import { defineComponent, PropType} from '@nuxtjs/composition-api'
import Artist from '~/utils/types/Artists'
export default defineComponent({
	props: {
		artists: {
        type: Array as PropType<Artist[]>,
        required: true
      },
      title: {
        type: String,
        required: false
      }
    },
	setup() {
		return {
		};
	},
})
</script>
<style scoped>
.v-card__title {
	font-size: 1.05rem !important;
	line-height: 1.5rem !important;
	word-break: break-word !important;
}
.artist-image{
	border-radius: 5px;
	width: 100%;
}
.artist-content:hover{
	cursor: pointer;
}
</style>
