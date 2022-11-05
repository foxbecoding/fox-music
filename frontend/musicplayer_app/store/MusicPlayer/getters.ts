import { GetterTree } from 'vuex';
import { RootState } from '~/store';
import { MusicPlayerState} from '~/store/MusicPlayer';
import Song from '~/utils/types/Songs';

const getters: GetterTree<MusicPlayerState, RootState> = {
    audio: state => state.audio,
    currentTime: state => state.currentTime,
    currentTimeStr: state => state.currentTimeStr,
    duration: state => state.duration,
    durationStr: state => state.durationStr,
    isActive: state => state.isActive as boolean,
    isEnded: state => state.isEnded as boolean,
    isLoop: state => state.isLoop as boolean,
    isMuted: state => state.isMuted as boolean,
    isPaused: state => state.isPaused as boolean,
    isSliding: state => state.isSliding as boolean,
    isShuffled: state => state.isShuffled as boolean,
    song: state => state.song as Song,
    songs: state => state.songs as Song[],
    songsConst: state => state.songsConst as Song[],
    volume: state => state.volume as number,
};

export default getters