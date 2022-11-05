<template>
	<div class="d-flex flex-no-wrap song-content-container">
        <div>
            <v-img max-width="40px" :src="`/assets/song_thumbnails/${SONG.thumbnail}`"/> 
        </div>
        <div class="song-details-container">
            <p class="mb-0 ml-1 song-title">{{SONG.title}}</p>
            <p class="mb-0 ml-1 artist-name-container">
                <span 
                    v-for="(artist, a) in SONG.artists"
                    :key="`artist_${a}`"
                >
                    <span
                        @click.stop="$router.push(`/artists/${artist.uniqid}`)" 
                        class="artist-name"
                    >
                        {{artist.name}}
                    </span>
                    <span class="artist-name__divider" v-if="a < SONG.artists.length - 1">/</span>
                </span>	
            </p>   
        </div>
    </div>
</template>
<script lang="ts">
import Song from '~/utils/types/Songs';
import { MusicPlayerState } from '~/store/MusicPlayer';
import { defineComponent, useStore, computed} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {     
        const store = useStore<MusicPlayerState>();
        const SONG = computed<Song>( 
            () => store.getters['MusicPlayer/song']
        );
        
		return { SONG };
	}
})
</script>
<style scoped>
.song-content-container{
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    max-width: 200px;
    width: 100%;
}
@media screen and (max-width: 960px) {
    .song-content-container{
        max-width: 130px;
    }
}
@media screen and (max-width: 600px) {
    .song-content-container{
        top: 0;
        transform: translateY(0);
        max-width: 250px;
    }
}
.song-details-container{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.song-title{
    font-size: 0.70rem;
    flex: 1 1 100%;
    text-overflow: ellipsis;
    overflow: hidden;
}

.artist-name-container{
    flex: 1 1 100%;
    position: relative;
    text-overflow: ellipsis;
    overflow: hidden;
    top: -6px;
}
.artist-name{
    font-size: 0.70rem;
    
}
.artist-name:hover{
	cursor: pointer;
	color: #2196F3;
}
.artist-name__divider{
    font-size: 0.70rem;
}
</style>
