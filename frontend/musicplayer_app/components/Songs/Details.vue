<template>
	<v-container class="px-4" fluid>
		<v-card
            color="rgb(3,3,3)"
            flat
          >
            <div v-if="$vuetify.breakpoint.smAndUp" class="d-flex flex-no-wrap">
                <v-avatar class="ma-3" size="125">
                    <v-img :src="`/assets/song_thumbnails/${song.thumbnail}`" />
                </v-avatar>
                <div class="song-details">
                    <v-card-title
                        class="py-1 text-h5"
                        v-text="song.title"
                    />
                    <v-card-title class="py-0 text-h5">
                        <span 
                            v-for="(artist, a) in song.artists"
                            :key="`artist_${a}`"
                        >
                            <span
                                @click="$router.push(`/artists/${artist.uniqid}`)" 
                                class="artist-name"
                            >{{artist.name}}</span>
                            <span class="mr-1" v-if="a < song.artists.length - 1">/</span>
                        </span>	
                    </v-card-title>
                </div>
            </div>
            <div v-else >
                <img 
                    style="width: 100%; border-radius: 4px;" 
                    :src="`/assets/song_thumbnails/${song.thumbnail}`" 
                />
                <v-card-title
                    class="py-1 song-details--mobile text-h5"
                    v-text="song.title"
                />
                <v-card-title class="py-0 song-details--mobile text-h5">
                    <span 
                        v-for="(artist, a) in song.artists"
                        :key="`artist_${a}`"
                        
                    >
                        <span
                            @click.stop="$router.push(`/artists/${artist.uniqid}`)" 
                            class="artist-name"
                        >{{artist.name}}</span>
                        <span v-if="a < song.artists.length - 1"> / </span>
                    </span>	
                </v-card-title>
            </div>
        </v-card>
	</v-container>
</template>
<script lang="ts">
import { defineComponent, PropType} from '@nuxtjs/composition-api'
import Song from '~/utils/types/Songs'
export default defineComponent({
    props: {
		song: {
        type: Object as PropType<Song>,
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
.song-details{
    position: relative;
    top: 50%;
    transform: translateY(25%);
}
.song-details--mobile{
    display: block;
    text-align: center;
    word-break: break-word !important;
}
.artist-name:hover{
	cursor: pointer;
	color: #2196F3;
}
</style>
