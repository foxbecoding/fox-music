<template>
	<v-container class="px-4" fluid>
		<v-card
            color="rgb(3,3,3)"
            flat
          >
            <div v-if="$vuetify.breakpoint.smAndUp" class="d-flex flex-no-wrap">
                <v-avatar class="ma-3" size="125">
                    <v-img :src="`/assets/${artist.img_file_path}`" />
                </v-avatar>
                <div>
                    <v-card-title
                        class="artist-name text-h4"
                        v-text="artist.name"
                    />
                </div>
            </div>
            <div v-else >
                <v-avatar rounded="lg" class="ma-3 artist-image--mobile" size="200">
                    <v-img :src="`/assets/${artist.img_file_path}`" />
                </v-avatar>
                <v-card-title
                    class="artist-name--mobile text-h5"
                    v-text="artist.name"
                />
            </div>
        </v-card>
	</v-container>
</template>
<script lang="ts">
import { defineComponent, PropType} from '@nuxtjs/composition-api'
import Artist from '~/utils/types/Artists'
export default defineComponent({
    props: {
		artist: {
        type: Object as PropType<Artist>,
        required: true
      }
    },
	setup() {
		return {
		};
	},
})
</script>
<style scoped>
.artist-name{
    position: relative;
    top: 50%;
    translate: 0 -50%;
}

.artist-image--mobile{
    display: block;
    margin-left: auto !important;
    margin-right: auto !important;
}
.artist-name--mobile{
    display: block;
    text-align: center;
    word-break: break-word !important;
}
</style>
