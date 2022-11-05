import { MusicPlayerState } from '~/store/MusicPlayer';

const currentSongIndex = (state: MusicPlayerState): number => {
    return state.songs.findIndex(song => song.uniqid == state.song.uniqid);
};
  
const timeFormat = (time: number): string => {
    var hrs = ~~(time / 3600);
    var mins = ~~((time % 3600) / 60);
    var secs = ~~time % 60;
    var ret = "";
  
    hrs > 0 ? ret += "" + hrs + ":" + (mins < 10 ? "0" : "") : '';
  
    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
};

export {
    currentSongIndex,
    timeFormat
}