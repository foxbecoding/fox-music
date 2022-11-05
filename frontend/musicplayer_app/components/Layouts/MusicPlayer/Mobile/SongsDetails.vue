<template>
	<v-row>
        <v-toolbar flat height="50" color="rgb(12,12,12)">  
            <div class="d-flex flex-no-wrap song-content-container">
                <div class="song-content-img">
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
            <v-spacer />
            <span style="font-size: 0.75rem">{{CURRENT_TIME_STR}}/{{DURATION_STR}}</span>
            <v-btn 
                class="now-playing-btn"
                :to="$route.name != 'playing-_id' ? `/playing/${SONG.uniqid}` : '/'" 
                icon
                small
            >
                <v-icon v-if="$route.name != 'playing-_id'">mdi-menu-up</v-icon>
                <v-icon v-else>mdi-menu-down</v-icon>
            </v-btn>
        </v-toolbar>
    </v-row>
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

        //computed
        const DURATION_STR = computed<string>(() => {
            return store.getters['MusicPlayer/durationStr']
        });
        const CURRENT_TIME_STR = computed<string>(() => {
            return store.getters['MusicPlayer/currentTimeStr']
        });

		return {
            DURATION_STR,
            CURRENT_TIME_STR,
            SONG
        };
	}
})
</script>
<style scoped>
.song-content-container{
    align-self: baseline;
    max-width: 180px;
    width: 100%;
}
.song-content-img{
    align-self: center;
}
.song-details-container{
    position: relative;
    top: 4px;
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
.now-playing-btn{
    z-index: 10
}
</style>
