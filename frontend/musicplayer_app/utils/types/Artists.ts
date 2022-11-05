import Song from '~/utils/types/Songs';
interface Artist {
    img_file_path: string;
    songs: Song[];
    name: string;
    uniqid: string;
};

export default Artist;